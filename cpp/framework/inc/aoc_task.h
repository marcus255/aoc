#pragma once

#include <string>
#include <stdexcept>
#include <vector>

class AocTask {
public:
    AocTask(std::string name, std::string answer1 = "", std::string answer2 = "");
    virtual ~AocTask() = default;

    virtual std::string part1Test() = 0;
    virtual std::string part1() = 0;
    virtual std::string part2Test() = 0;
    virtual std::string part2() = 0;

    void run();

protected:
    std::string answer1;
    std::string answer2;
    std::vector<std::string> test_input;
    std::vector<std::string> task_input;

private:
    void parseName();
    void openInputFiles();

    std::string year{};
    std::string day{};
    std::string name;
};