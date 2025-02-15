#include "../inc/argument_parser.h"
#include <iostream>

std::optional<std::variant<bool, std::string>> parseArgument(const std::string& arg, const std::unordered_map<std::string, std::variant<bool, std::string>>& options) {
    auto it = options.find(arg);
    if (it != options.end()) {
        return it->second;
    }
    return std::nullopt;
}

void parseArguments(int argc, char* argv[], bool& runAll, bool& runLast, std::string& singleTask, std::string& year) {
    std::unordered_map<std::string, std::variant<bool, std::string>> options = {
        {"--last", true},
        {"--all", ""},
        {"--task", ""},
        // TODO: add verbose option
    };

    for (int i = 1; i < argc; ++i) {
        std::string arg = argv[i];
        auto result = parseArgument(arg, options);
        if (result) {
            if (std::holds_alternative<bool>(*result)) {
                if (arg == "--last") {
                    runLast = true;
                }
            } else if (std::holds_alternative<std::string>(*result)) {
                if (arg == "--all") {
                    runAll = true;
                    if (i + 1 < argc && argv[i + 1][0] != '-') {
                        year = argv[++i];
                    } else {
                        year = "2024";
                    }
                } else if (arg == "--task" && i + 1 < argc) {
                    singleTask = argv[++i];
                }
            }
        } else {
            showHelp(argv[0]);
            exit(1);
        }
    }
}

void showHelp(const char* programName) {
    std::cerr << "Usage: " << programName << " [--last] [--all <year>] [--task <task_name>]" << std::endl;
}