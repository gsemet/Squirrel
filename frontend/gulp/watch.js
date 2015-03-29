'use strict';

var gulp = require('gulp');

var paths = gulp.paths;

gulp.task('watch', ['markups', 'inject', 'pot', 'translations'], function() {
  gulp.watch([
    paths.src + '/*.html',
    paths.src + '/{app,components,services}/**/*.less',
    paths.src + '/{app,components,services}/**/*.js',
    paths.src + '/po/*.js',
    paths.src + '/index.js',
    paths.src + '/index.less',
    'bower.json',
    'gulp/*.js',
  ], ['inject', 'pot', 'translations']);
  gulp.watch(paths.src + '/{app,components,services}/**/*.jade', ['markups']);
});
