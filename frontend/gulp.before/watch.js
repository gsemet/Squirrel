'use strict';

var gulp = require('gulp');

var paths = gulp.paths;

gulp.task('watch', ['markups', 'inject', 'pot', 'translations'], function() {
  gulp.watch([
    paths.src + '/*.html',
    paths.src + '/{app,modules}/**/*.less',
    paths.src + '/{app,modules}/**/*.css',
    paths.src + '/{app,modules}/**/*.jade',
    paths.src + '/{app,modules}/**/*.html',
    paths.src + '/{app,modules}/**/*.js',
    paths.src + '/{app,modules}/**/*.coffee',
    paths.src + '/languages/*.json',
    paths.src + '/index.*',
    paths.src + '/vendor.less',
    'bower.json',
    'gulp/*.js',
  ], ['inject', 'pot', 'translations']);
  gulp.watch(paths.src + '/{app,modules}/**/*.jade', ['markups']);
  gulp.watch(paths.src + '/po/*.po', ['translations']);
});
