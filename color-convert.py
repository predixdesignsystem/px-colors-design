import json
import sys
import re

def convertFile():
    colors = {}
    dvColors = {}
    dvOrder = []

    #open scss file and do a regex search for color vars and values
    with open(sys.argv[1], 'r') as scss:
        reColorStr = r"\s?\$((dv-)?\w+(-?\w+)+)\s+:\s+(rgb\(\d+,\d+,\d+\))"
        reColor = re.compile(reColorStr)
        for line in scss:
            results = reColor.search(line)
            if(results):
                #if it starts dv, then it is a data vis color
                if(results.group(2)):
                    dvColors[results.group(1)] = results.group(4)
                    dvOrder.append(results.group(1))
                #else it is a general color
                else:
                    colors[results.group(1)] = results.group(4)
    scss.close()
    #add in our grey values = to gray
    grey = {}
    for c in colors:
      if c[:-1] == 'gray':
        key = 'grey' + c[-1]
        grey[key] = colors[c]

    colors.update(grey)

    #same in DV
    dvGrey = {}
    for dv in dvColors:
      dvl = dv.split('-')
      if dvl[-1] == 'gray':
        dvl[-1] = 'grey'
        key = '-'.join(dvl)
        dvGrey[key] = dvColors[dv]

    dvColors.update(dvGrey)

    with open(sys.argv[2], 'w') as js:
        js.write('<script>\n')
        js.write('/*\nName:\ncommonColors\n\nDescription:\n\nPolymer behavior that provides the basic color definitions. Colors match (and are generated from) px-colors-design SCSS.\nThis allows access to the color definitions in javascript for applications where CSS is not ideal.\n\nDependencies:\n- none\n\n@polymerBehavior commonColors\n\n*/\n\n')
        js.write('var commonColors = {\n\n')
        js.write('{:<2}{}'.format('','properties: {\n'))

        js.write('{:<4}{}'.format('','/**\n'))
        js.write('{:<4}{}'.format('','* colors\n'))
        js.write('{:<4}{}'.format('','* Defines RBG values for each color.\n'))
        js.write('{:<4}{}'.format('','*\n'))
        js.write('{:<4}{}'.format('','* Format: Object\n'))
        js.write('{:<4}{}'.format('','*/\n'))

        js.write('{:<4}{}'.format('','colors:{\n'))
        js.write('{:<6}{}'.format('','type:Object,\n'))
        js.write('{:<6}{}'.format('','value:'))
        js.write(json.dumps(colors,indent=8, separators=(',', ': ')))
        js.write('{}'.format('\n'))
        js.write('{:<4}{}'.format('','},\n'))


        js.write('{:<4}{}'.format('','/**\n'))
        js.write('{:<4}{}'.format('','* seriesColorOrder\n'))
        js.write('{:<4}{}'.format('','* Defines RBG values for each data vis color\n'))
        js.write('{:<4}{}'.format('','*\n'))
        js.write('{:<4}{}'.format('','* Format: Object\n'))
        js.write('{:<4}{}'.format('','*/\n'))

        js.write('{:<4}{}'.format('','dataVisColors:{\n'))
        js.write('{:<6}{}'.format('','type:Object,\n'))
        js.write('{:<6}{}'.format('','value:'))
        js.write(json.dumps(dvColors,indent=8, separators=(',', ': ')))
        js.write('{}'.format('\n'))
        js.write('{:<4}{}'.format('','},\n'))


        js.write('{:<4}{}'.format('','/**\n'))
        js.write('{:<4}{}'.format('','* seriesColorOrder\n'))
        js.write('{:<4}{}'.format('','* Defines an order that colors should be used in for multiple series\n'))
        js.write('{:<4}{}'.format('','*\n'))
        js.write('{:<4}{}'.format('','* Format: Array\n'))
        js.write('{:<4}{}'.format('','*/\n'))

        js.write('{:<4}{}'.format('','seriesColorOrder:{\n'))
        js.write('{:<6}{}'.format('','type:Array,\n'))
        js.write('{:<6}{}'.format('','value:'))
        js.write(json.dumps(dvOrder,indent=8, separators=(',', ': ')))
        js.write('{}'.format('\n'))
        js.write('{:<4}{}'.format('','},\n'))


        js.write('{:<2}{}'.format('','}\n'))
        js.write('};\n')
        js.write('</script>\n')

    js.close()
    print "done"
if __name__ == "__main__":
    convertFile()
