#include "DefaultScheduleSet.hpp"

namespace openstudio {
namespace model {
DefaultScheduleSet::DefaultScheduleSet() = default;

std::string DefaultScheduleSet::getDefaultSchedule(const DefaultScheduleType& defaultScheduleType) const {
  return defaultScheduleType.valueName();
}
}  // namespace model
}  // namespace openstudio
