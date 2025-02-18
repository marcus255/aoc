#pragma once

#include <string>
#include <stdexcept>
#include <vector>
#include <functional>
#include <any>


class AocTask {
    using StrVector = std::vector<std::string>;

    enum class TaskType {
        Test,
        Task,
    };

public:
    AocTask(std::string name, std::string answer1 = "", std::string answer2 = "") noexcept(false);
    virtual ~AocTask() = default;

    virtual std::string partOneSolution(const StrVector& input) = 0;
    virtual std::string partTwoSolution(const StrVector& input) = 0;

    virtual bool isTestMode() const { return testMode; }
    void run();

private:
    void parseName();
    void loadInputFile(TaskType type);
    void runTest(const std::string &prefix, const StrVector& input, const std::string& expectedAnswer,
        const std::function<std::string(const StrVector&)>& solutionFunc);
    void runTask(const std::string &prefix, const StrVector& input,
        const std::function<std::string(const StrVector&)>& solutionFunc);

    std::string year{};
    std::string day{};
    std::string name{};
    bool testMode{false};

protected:
    std::string answer1;
    std::string answer2;
    StrVector testInput;
    StrVector taskInput;
    std::any testData;
    std::any taskData;
};