#include "model/DefaultScheduleSet.hpp"
#include "utilities/bcl/BCLEnums.hpp"
#include <fmt/core.h>

int main() {
  openstudio::MeasureType t(openstudio::MeasureType::ModelMeasure);
  fmt::print("MeasureType: {}, {}\n", t.valueName(), t.valueDescription());

  openstudio::model::DefaultScheduleSet d;
  fmt::print("DefaultScheduleType: {}\n", d.getDefaultSchedule(openstudio::model::DefaultScheduleType::HoursofOperationSchedule));
}
