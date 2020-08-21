with import <nixpkgs> {};
stdenv.mkDerivation {
  name = "awesfx-0.5.2-sf2text";
  buildInputs = [ automake autoconf ];
  src = pkgs.fetchFromGitHub {
    owner = "tiwai";
    repo = "awesfx";
    rev = "v0.5.2";
    sha256 = "1hhqbb7c6iy9yhyi240jh2k39x01i7hs2w1zsv287jac708pcjkh";
  };
  patches = [ ./sf2text.patch ];
  configurePhase = ''
    autoreconf -fi
    ./configure --prefix=$out
  '';
}
