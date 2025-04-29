{
  description = "Webscraping Dev Environment";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  inputs.flake-utils.url = "github:numtide/flake-utils";

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        glib = pkgs.glib.out;
      in
      {
        devShells.default = pkgs.mkShell {
          name = "webscraper-dev";
          buildInputs = [
  pkgs.python311
  pkgs.python311Packages.selenium
  pkgs.chromium
  pkgs.chromedriver
  pkgs.curl
  pkgs.git
  pkgs.unzip
];

          shellHook = ''
            echo "Dev environment ready."
            if [ -z "$GH_TOKEN" ]; then
              echo "⚠️  Warning: GH_TOKEN is not set! GitHub operations may fail."
            else
              echo "✅ GH_TOKEN is set."
            fi

            export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${glib}/lib
          '';
        };
      });
}
