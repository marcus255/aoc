#pragma once

#include <string>
#include <unordered_map>
#include <optional>
#include <variant>

std::optional<std::variant<bool, std::string>> parseArgument(const std::string& arg, const std::unordered_map<std::string, std::variant<bool, std::string>>& options);

void parseArguments(int argc, char* argv[], bool& runAll, bool& runLast, std::string& singleTask, std::string& year);

void showHelp(const char* programName);