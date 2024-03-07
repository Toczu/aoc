local file = io.open("input.txt", "r")

local lines = {}

if file then
    for line in file:lines() do
        table.insert(lines, tonumber(line))
    end
    file:close()
end

local sum = 0
for i, v in ipairs(lines) do
    if i < 2 then goto continue end
    if v > lines[i - 1] then sum = sum + 1 end
    ::continue::
end

print(sum)
