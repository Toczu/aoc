local lfs = require("lfs")
local term = require("term")

-- Function to list subdirectories
local function listSubdirectories(path)
    local subdirectories = {}
    for entry in lfs.dir(path) do
        if entry ~= "." and entry ~= ".." then
            local fullPath = path .. "/" .. entry
            local attributes = lfs.attributes(fullPath)
            if attributes.mode == "directory" then
                table.insert(subdirectories, entry)
            end
        end
    end
    table.sort(subdirectories, function(a, b) return a < b end)
    return subdirectories
end

-- Function to list Lua files
local function listLuaFiles(path)
    local luaFiles = {}
    for entry in lfs.dir(path) do
        if entry ~= "." and entry ~= ".." then
            local fullPath = path .. "/" .. entry
            local attributes = lfs.attributes(fullPath)
            if attributes.mode == "file" and string.sub(entry, -4) == ".lua" then
                table.insert(luaFiles, entry)
            end
        end
    end
    table.sort(luaFiles, function(a, b) return a < b end)
    return luaFiles
end

-- Function to handle user input
local function handleUserInput(path)
    while true do
        local parentPath = string.match(path, "(.-)[^/]-$")
        term.clear()

        print("Current directory: " .. path)
        print("Options:")
        print("0. Go up one directory")

        local subdirectories = listSubdirectories(path)
        for i, subdir in ipairs(subdirectories) do
            print(i .. ".\t" .. subdir)
        end

        local luaFiles = listLuaFiles(path)
        for i, file in ipairs(luaFiles) do
            print(i + #subdirectories .. ".\t" .. file)
        end

        io.write("Enter your choice: ")
        local choice_string = io.read()
        local choice = tonumber(choice_string)

        if choice == 0 then
            if parentPath ~= "" then
                path = parentPath
            end
        elseif choice and choice <= #subdirectories then
            path = path .. "/" .. subdirectories[choice]
        elseif choice and choice <= #subdirectories + #luaFiles then
            local fileIndex = choice - #subdirectories
            local filePath = path .. "/" .. luaFiles[fileIndex]
            print("Do you want to run the file in test mode? (y/n)")
            local runInTestMode = io.read()
            print("Running " .. filePath .. "...")
            if runInTestMode:lower() == "y" then
                print("Running in test mode...")
                os.execute("lua " .. filePath .. " -p " .. path .. " -t")
                os.exit(0)
            else
                os.execute("lua " .. filePath .. " -p " .. path)
                os.exit(0)
            end
        else
            print("Invalid choice!")
        end
    end
end

-- Start the program
handleUserInput(".")
