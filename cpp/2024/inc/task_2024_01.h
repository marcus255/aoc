#pragma once

// TODO: fix relative paths
#include "../../framework/inc/aoc_task.h"
#include <string>

class Task_2024_01 : public AocTask {
public:
    Task_2024_01();

    std::string part1Test() override;
    std::string part1() override;

    std::string part2Test() override;
    std::string part2() override;
};