#!/usr/bin/Rscript

pkgLoad <- function( packages = "favourites" ) {

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

pkgLoad()