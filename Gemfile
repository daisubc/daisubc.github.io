source "https://rubygems.org"

# GitHub Pages gem includes Jekyll and all supported plugins
gem "github-pages", group: :jekyll_plugins

# Windows compatibility (only installed on Windows)
install_if -> { RUBY_PLATFORM =~ %r!mingw|mswin|java! } do
  gem "tzinfo", "~> 1.2"
  gem "tzinfo-data"
end
gem "wdm", "~> 0.1.0", :install_if => Gem.win_platform?
