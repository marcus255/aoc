#include "../inc/argument_parser.h"
#include <iostream>

std::optional<std::variant<bool, std::string>> parseArgument(const std::string& arg, const std::unordered_map<std::string, std::variant<bool, std::string>>& options) {
    auto it = options.find(arg);
    if (it != options.end()) {
        return it->second;
    }
    return std::nullopt;
}

void parseArguments(int argc, char* argv[], bool& runAll, bool& runLast, std::string& singleTask) {
    std::unordered_map<std::string, std::variant<bool, std::string>> options = {
        {"--last", true},
        {"--all", true},
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
                } else if (arg == "--all") {
                    runAll = true;
                }
            } else if (std::holds_alternative<std::string>(*result) && i + 1 < argc) {
                singleTask = argv[++i];
            }
        } else {
            std::cerr << "Usage: " << argv[0] << " [--last] [--all] [--task <task_name>]" << std::endl;
            exit(1);
        }
    }
}

void showHelp(const char* programName) {
    std::cerr << "Usage: " << programName << " [--last] [--all] [--task <task_name>]" << std::endl;
}