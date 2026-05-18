/***********************************************************************************************************************
*  OpenStudio(R), Copyright (c) Alliance for Energy Innovation, LLC.
*  See also https://openstudio.net/license
***********************************************************************************************************************/

#ifndef MODEL_DEFAULTSCHEDULESET_HPP
#define MODEL_DEFAULTSCHEDULESET_HPP

#include "ModelAPI.hpp"

#include "../utilities/core/Enum.hpp"

namespace openstudio {
namespace model {
// clang-format off

  OPENSTUDIO_ENUM(DefaultScheduleType,
    ((HoursofOperationSchedule)(Hours of Operation Schedule)(1))
    ((NumberofPeopleSchedule)(Number of People Schedule)(2))
    ((PeopleActivityLevelSchedule)(People Activity Level Schedule)(3))
    ((LightingSchedule)(Lighting Schedule)(4))
    ((ElectricEquipmentSchedule)(Electric Equipment Schedule)(5))
    ((GasEquipmentSchedule)(Gas Equipment Schedule)(6))
    ((HotWaterEquipmentSchedule)(Hot Water Equipment Schedule)(7))
    ((InfiltrationSchedule)(Infiltration Schedule)(8))
    ((SteamEquipmentSchedule)(Steam Equipment Schedule)(9))
    ((OtherEquipmentSchedule)(Other Equipment Schedule)(10))
    ((DesignPowerInputScheduleName)(Design Power Input Schedule)(11))
    ((CPULoadingScheduleName)(CPU Loading Schedule)(12))
  );

// clang-format on

class MODEL_API DefaultScheduleSet
{
 public:
  explicit DefaultScheduleSet();

  std::string getDefaultSchedule(const DefaultScheduleType& defaultScheduleType) const;
};

}  // namespace model
}  // namespace openstudio

#endif  // MODEL_DEFAULTSCHEDULESET_HPP
