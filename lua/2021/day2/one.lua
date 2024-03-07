local file = io.open("input.txt", "r")

local horizontal = 0
local depth = 0

if file then
    for line in file:lines() do
        for k, v in string.gmatch(line, "(%w+) (%w+)") do
            if k == "forward" then
                horizontal = horizontal + tonumber(v)
            elseif k == "up" then
                depth = depth - tonumber(v)
            else
                depth = depth + tonumber(v)
            end
        end
        -- table.insert(lines, tonumber(line))
    end
    file:close()
end

print('horizontal\t', horizontal)
print('depth\t', depth)
print('Solution:\t', horizontal * depth)

