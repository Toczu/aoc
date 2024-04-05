local file = io.open("test.txt", "r")
local rows = {}

if file then
    for line in file:lines() do
        local j = 1
        for digit in line:gmatch("%d") do
            rows[j] = (rows[j] or '') .. digit
            j = j + 1
        end
    end
    file:close()
end

local t = {}

for i, v in ipairs(rows) do
    local j, k = 0, 0
    for digit in v:gmatch("%d") do
        if digit == '1' then j = j + 1 else k = k + 1 end
    end
    t[i] = (j > k) and '1' or '0'
end

local s = table.concat(t)

local epsilon_str = ''
for i = 1, s:len() do
    epsilon_str = epsilon_str .. (s:sub(i, i) == '1' and '0' or '1')
end
local epsilon = tonumber(epsilon_str, 2)

local gamma = tonumber(s, 2)
print(gamma * epsilon)
