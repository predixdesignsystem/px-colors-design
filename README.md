# Colors

The Colors module assigns Sass variables to the PX color palette.

## Installation

Install this module using bower:

    bower install --save https://github.com/PredixDev/px-colors-design.git

Once installed, `@import` into your project's Sass file in its Settings layer:

    @import "px-colors-design/_settings.colors.scss";


## Behavior
Install this as a Polymer behavior:

    bower install --save https://github.com/PredixDev/px-colors-design.git

Then reference it in your project

    <link rel="import" href="../px-colors-design/colors.html" />

And add the variable as a behavior

    <script>
      Polymer({
        is: 'px-my-component',
        behaviors: [commonColors],
        ...
