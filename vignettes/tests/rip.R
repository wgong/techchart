#!/usr/bin/env Rscript
# this script helps with package install/uninstall
# similar to pip in python
suppressPackageStartupMessages(library("argparse"))

# create parser object
parser <- ArgumentParser()
parser$add_argument("-i", "--install", 
                    help = "install pkg(s) given here or from a file")
parser$add_argument("-u", "--uninstall", 
                    help = "uninstall pkg(s) given here or from a file")
args <- parser$parse_args()


pkgInstall <- function(packages) {

    if( length( packages ) == 1L && packages == "favourites" ) {
        packages <- c( "data.table", "chron", "plyr", "dplyr", "shiny",
            "shinyjs", "parallel", "devtools",  "utils",
            "stats", "ggplot2", "readxl",
            "feather", "readr", "DT", "knitr",
            "rmarkdown", "Rcpp"
        )
    }

    packagecheck <- match( packages, utils::installed.packages()[,1] )

    packagestoinstall <- packages[ is.na( packagecheck ) ]

    if( length( packagestoinstall ) > 0L ) {
        utils::install.packages( packagestoinstall,
                             repos = "https://cran.r-project.org/"
        )
    } else {
        print( "All requested packages already installed" )
    }

    for( package in packages ) {
        suppressPackageStartupMessages(
            library( package, character.only = TRUE, quietly = TRUE )
        )
    }

}

print(args)

if (!is.na(args$install)) {
  print("Install pkgs:", args$install[1])
}

# if (args$uninstall) {
#   print("Uninstall pkgs:", args$uninstall)
# }