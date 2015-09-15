'use strict';

var gulp = require('gulp');

var paths = gulp.paths;

var gettext = require('gulp-angular-gettext');
var debug = require('gulp-debug');

gulp.task('pot', function() {
  return gulp.src([
      'src/index.html',
      'src/{app,modules}/**/*.html',
      'src/{app,modules}/**/*.js'])
    .pipe(gettext.extract('template.pot', {
      // options to pass to angular-gettext-tools...
    }))
    .pipe(gulp.dest('src/po/'));
});

gulp.task('translations', function() {
  return gulp.src([
      'src/po/**/*.po',
    ])
    .pipe(debug({
      title: 'compile po:'
    }))
    .pipe(gettext.compile({
      format: "json"
    }))
    .pipe(gulp.dest('src/po/'));
});
