This file provides the developer's feedback comparing the current implementation to one developed 5 years ago.

- Due to unclear specifications on how user coordinates should be obtained, two versions of the program were implemented:
  1. **Static version**: Follows the parameter order specified in the [Input](./README.md#Input) section, where coordinates are provided as command-line arguments.
  2. **Live version**: Does not require coordinate arguments, instead retrieving them dynamically using live geolocation, as mentioned in the [Overview](./README.md#Overview).
- Any future changes requested regarding the coordinate input issue will be addressed as needed.
- The note in the requirements stating "all coordinates lie on a plane" is not applicable when using geographic coordinates (such as those from IP-based geolocation services). Therefore, for better accuracy, geodesic distances were calculated using the popular Python library `geopy`.
