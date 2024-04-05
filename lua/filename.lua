local argparse = require("argparse")

local parser = argparse("script", "An example.")
parser:option("-p --path", "Input file.", "")
parser:flag("-t --test", "Run in test mode")

local args = parser:parse()

---@diagnostic disable: lowercase-global
filename = args.path .. "/"

if args.test then
    filename = filename .. "test.txt"
else
    filename = filename .. "input.txt"
end
