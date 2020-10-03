import json

with open("hangars.json", "r") as input_file:
  with open("hangars.osm", "w") as output_file:
    input_json = json.loads(input_file.read())

    # This works as long as I don't have to worry about escaping.
    # ToDo: Switch to proper XML library
    output_file.write("<?xml version='1.0' encoding='UTF-8'?>\n")
    output_file.write("<osm version='0.6' generator='marekventur/hackney-bike-hangars'>\n")
    id=0;
    for hangar in input_json["hangers"].values():
      id -= 1
      output_file.write("  <node id='" + str(id) + "' action='modify' visible='true' lat='" + str(hangar["lat"]) + "' lon='" + str(hangar["long"]) + "'>\n")
      output_file.write("    <tag k='amenity' v='bicycle_parking' />\n")
      output_file.write("    <tag k='bicycle_paking' v='lockers' />\n")
      output_file.write("    <tag k='capacity' v='" + hangar["spaces"] + "' />\n")
      output_file.write("    <tag k='locked' v='yes' />\n")
      output_file.write("    <tag k='fee' v='yes' />\n")
      output_file.write("    <tag k='description' v='London Borough of Hackney Bicycle Hangar. Internal name \"" + hangar["hanger_id"] + "\"' />\n")
      output_file.write("    <tag k='operator' v='London Borough of Hackney' />\n")
      output_file.write("    <tag k='ownership' v='municipal' />\n")
      output_file.write("    <tag k='start_date' v='" + hangar["created"][0:9] + "' />\n")
      output_file.write("  </node>\n")
    output_file.write("</osm>\n")





