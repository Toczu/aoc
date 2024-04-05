local file = io.open("one.txt", "r")

local lines = {}

if file then
    for line in file:lines() do
        table.insert(lines, tonumber(line))
    end
    file:close()
end

local answer = -1
local prev = 0
for i, v in ipairs(lines) do
    if i < 3 then
        goto continue
    end
    local sum = v + lines[i - 1] + lines[i - 2]
    if sum > prev then answer = answer + 1 end
    prev = sum
    ::continue::
end

print(answer)
