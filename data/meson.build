install_data(
    'chardata',
    install_dir: join_paths(datadir, application_id)
)


install_data(
    'quickchar-autostart.desktop',
    install_dir: join_paths(sysconfdir, 'xdg', 'autostart')
)

install_data(
    'quickchar.bde',
    install_dir: join_paths(datadir, 'budgie-extras-daemon')
)

meson.add_install_script(
  'meson_post_install.py',
  datadir,
  bindir,
  pkgdatadir,
  application_id
)
