# Colors

The Colors module assigns Sass variables to the Predix Experience color palette.

## Installation

Install this module using bower:

    bower install --save https://github.sw.ge.com/pxc/px-colors-design.git

Once installed, `@import` into your project's Sass file in its Settings layer:

    @import "../px-tables-design/settings.colors";

#### A note about relative @import paths

Paths to a project's Bower dependencies differ depending on whether you are in the project itself (dependencies in some
a Bower managed directory in the project) vs. using the project 'downstream' (dependencies are siblings of the project).
Ideally we want to be able to 'build' in both cases without a lot of magic.

For Sass imports, can use the 'includePaths' option on the Grunt sass task to name a starting point to look for
relative paths. IncludePath 'bower_components/*' in the 'sass' task allows the actual @import paths in Sass files to start
with '../' so that they will resolve in either case described above and make editors happy.
