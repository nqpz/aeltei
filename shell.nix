# Use this file with nix-shell or similar tools; see https://nixos.org/
with import <nixpkgs> {};

let
  python = import ./nix/requirements.nix { inherit pkgs; };
in
mkShell {
  buildInputs = [
    (import ./nix/sf2text.nix)
    python.packages.mingus
  ];

  shellHook = ''
    export LIBRARY_PATH=${fluidsynth_1}/lib:$LIBRARY_PATH
    export LD_LIBRARY_PATH=${fluidsynth_1}/lib:$LD_LIBRARY_PATH
    export SOUNDFONT=${soundfont-fluid}/share/soundfonts/FluidR3_GM2-2.sf2
  '';
}
