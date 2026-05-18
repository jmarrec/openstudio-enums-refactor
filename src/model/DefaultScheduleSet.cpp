#include "DefaultScheduleSet.hpp"

#include <utilities/idd/IddEnums.hxx>

namespace openstudio {
namespace model {

DefaultScheduleSet::DefaultScheduleSet() : ModelObject(DefaultScheduleSet::iddObjectType()) {}

IddObjectType DefaultScheduleSet::iddObjectType() {
  return {IddObjectType::OS_DefaultScheduleSet};
}

std::string DefaultScheduleSet::getDefaultSchedule(const DefaultScheduleType& defaultScheduleType) const {
  return defaultScheduleType.valueName();
}
}  // namespace model
}  // namespace openstudio
