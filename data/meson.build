install_data(
    'chardata',
    install_dir: join_paths(datadir, application_id)
)


install_data(
    'quickchar-autostart.desktop',
    install_dir: xdg_appdir
)

substprog = find_program('subst.py')
desktopfile = custom_target('desktopfile',
  output : 'quickchar.desktop',
  input : 'quickchar.desktop.in',
  command : [substprog, '@INPUT@', pkgdatadir, '@OUTPUT@'],
  install : true,
  install_dir : join_paths(datadir, 'applications')
)

install_data(
    'quickchar.bde',
    install_dir: join_paths(datadir, 'budgie-extras-daemon')
)

install_data(
    'org.ubuntubudgie.quickchar.svg',
    install_dir: join_paths(datadir, 'icons', 'hicolor', 'scalable', 'apps')
)

meson.add_install_script(
  'meson_post_install.py',
  datadir,
  bindir,
  pkgdatadir,
  application_id
)
