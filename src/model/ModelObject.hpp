/***********************************************************************************************************************
*  OpenStudio(R), Copyright (c) Alliance for Energy Innovation, LLC.
*  See also https://openstudio.net/license
***********************************************************************************************************************/

#ifndef MODEL_MODELOBJECT_HPP
#define MODEL_MODELOBJECT_HPP

#include "ModelAPI.hpp"

#include "../utilities/idd/IddEnums.hpp"

#ifdef USE_NEW_ENUMS
#  include <utilities/idd/IddEnums.hxx>
#endif

namespace openstudio {

namespace model {

class MODEL_API ModelObject
{
 public:
 protected:
  explicit ModelObject(IddObjectType type);

 private:
  IddObjectType m_iddObjectType;
};
}  // namespace model
}  // namespace openstudio

#endif
