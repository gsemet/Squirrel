<sidebar-with-content/>
=======================

Two main features:

Don't use route for page navigation

    Independent from ``UI Router`` or ``ngRouge``.

    Allow to define several, independent sidebar on different part of your web site.

    Also, this doesn't force you to define all your pages in the main config page, thus allowing you
    to componentize your code more easily. Of course, all custom, sidebar only "states", are only
    activated if the sidebar state or route is enabled.

``sb-sref`` directive

    Directly inspirated from UI Router's ``ui-sref`` directive, this simplifies this jump between
    two pages, outside of a click on a link in the sidebar.

    Syntax is::

      <a sb-sref="page_name"></a>

    ``page_name`` is the name of the page or subpage where to jump.

    ``href`` is automatically added.
