'use strict';

var gulp = require('gulp');

var paths = gulp.paths;

var gettext = require('gulp-angular-gettext');

gulp.task('pot', function() {
  return gulp.src([
      'src/index.html',
      'src/{app,components,services,directives,filters}/**/*.html',
      'src/{app,components,services,directives,filters}/**/*.js'])
    .pipe(gettext.extract('template.pot', {
      // options to pass to angular-gettext-tools...
    }))
    .pipe(gulp.dest('src/po/'));
});

gulp.task('translations', function() {
  return gulp.src([
      'src/po/**/fr.po',
    ])
    .pipe(gettext.compile({}))
    .pipe(gulp.dest('src/po/'));
});
