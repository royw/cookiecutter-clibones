{ pkgs ? import <nixpkgs> {} # here we import the nixpkgs package set
}:
pkgs.mkShell {               # mkShell is a helper function
  name="dev-environment";    # that requires a name
  buildInputs = [            # and a list of packages
    pkgs.python3
    pkgs.python3Packages.virtualenv
    pkgs.mypy
    pkgs.cookiecutter
  ];
  shellHook = ''             # bash to run when you enter the shell
  echo "Start developing..."
  '';
}