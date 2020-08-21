with import <nixpkgs> {};
let python = import ./requirements.nix { inherit pkgs; };
in
stdenv.mkDerivation {
  name = "aeltei";
  buildInputs = [
    (import ./sf2text.nix)
    python.packages.mingus
  ];

  shellHook = ''
    export LIBRARY_PATH=${fluidsynth_1}/lib:$LIBRARY_PATH
    export LD_LIBRARY_PATH=${fluidsynth_1}/lib:$LD_LIBRARY_PATH
    export SOUNDFONT=${soundfont-fluid}/share/soundfonts/FluidR3_GM2-2.sf2
  '';
}
