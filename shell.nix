# Use this file with nix-shell or similar tools; see https://nixos.org/
with import <nixpkgs> {};

let
  pkgs = import (builtins.fetchTarball {
    name = "nixpkgs-unstable-ghc844";
    url = "https://github.com/nixos/nixpkgs/archive/8ffedd83693d6effd1c271f3ad17c38f7dcecf42.tar.gz";
    sha256 = "1c2m2b0dslqkcwhg1yfh1mhfkc83xs1j78w9m4a2ymgcp370srs2";
  }) {};
  python = import ./nix/requirements.nix { inherit pkgs; };
in
mkShell {
  buildInputs = [
    (import ./nix/sf2text.nix)
    python.packages.mingus
  ];

  shellHook = ''
    export LIBRARY_PATH=${pkgs.fluidsynth_1}/lib:$LIBRARY_PATH
    export LD_LIBRARY_PATH=${pkgs.fluidsynth_1}/lib:$LD_LIBRARY_PATH
    export SOUNDFONT=${pkgs.soundfont-fluid}/share/soundfonts/FluidR3_GM2-2.sf2
  '';
}
