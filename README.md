# Colors

The Colors module assigns Sass variables to the PX color palette.

## Installation

Install this module using bower:

    bower install --save px-colors-design

Once installed, `@import` into your project's Sass file in its Settings layer:

    @import "px-colors-design/_settings.colors.scss";


## Behavior
This component can also be installed as a Polymer behavior:

    bower install --save px-colors-design

Then reference it in your project

    <link rel="import" href="../px-colors-design/colors.html" />

And add the variable as a behavior

    <script>
      Polymer({
        is: 'px-my-component',
        behaviors: [commonColors],
        ...
      });
    </script>
