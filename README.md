# techchart

The goal of this R package (techchart) is to provide a comprehensive set of tools and methods for automated technical analysis. This includes trend analysis, automated support and resistance, technical pattern and technical formation identification.

## Installation

You can install from github with:

```R
# install.packages("devtools")
devtools::install_github("prodipta/techchart")
# this includes some codes in C++, and hence will require RTools (windows) or Xcode (Mac) and compilers/ libraries for building from source
```
## Example

Please see the package [vignette](vignettes/techchart.md) for detailed explanation and examples of the functionalities. Alternatively refer to [my blog](http://prodiptag.blogspot.com/2016/10/systematic-trading-r-package-for.html) for a discussion.


## setup R on Ubuntu

### Install R core

https://www.digitalocean.com/community/tutorials/how-to-install-r-on-ubuntu-22-04

```
$ wget -qO- https://cloud.r-project.org/bin/linux/ubuntu/marutter_pubkey.asc | sudo gpg --dearmor -o /usr/share/keyrings/r-project.gpg

$ echo "deb [signed-by=/usr/share/keyrings/r-project.gpg] https://cloud.r-project.org/bin/linux/ubuntu jammy-cran40/" | sudo tee -a /etc/apt/sources.list.d/r-project.list

$ sudo apt update

$ sudo apt install --no-install-recommends r-base  
# Setting up r-base-core (4.2.2.20221110-1.2204.0) 

$ sudo -i R   # launch R

> install.packages('txtplot')
# Installing package into ‘/usr/local/lib/R/site-library’

> library('txtplot')
# load lib

> help(txtplot)

> txtdensity(rnorm(500))
# plot normal dist

> cars   
# list data

> txtplot(cars[,1], cars[,2], xlab = 'speed', ylab = 'distance')
# text plot distance vs speed

> q()         # exit
```

### Install RStudio
https://www.digitalocean.com/community/tutorials/how-to-set-up-rstudio-on-an-ubuntu-cloud-server

```
$ dpkg -l         # list all installed pkg
$ dpkg -S r-base  # list a named pkg
$ dpkg -l | grep r-base

ii  libgcr-base-3-1:amd64                                       3.40.0-4                                            amd64        Library for Crypto related tasks
ii  r-base                                                      4.2.2.20221110-1.2204.0                             all          GNU R statistical computation and graphics system
ii  r-base-core                                                 4.2.2.20221110-1.2204.0                             amd64        GNU R core of statistical computation and graphics system

$ sudo apt-get install r-base libapparmor1 gdebi-core
$ wget https://download1.rstudio.org/electron/jammy/amd64/rstudio-2022.12.0-353-amd64.deb -O rstudio.deb

$ sudo apt-get update
$ sudo gdebi rstudio.deb

$ sudo adduser rstudio  # add user

$ sudo apt-get install gfortran libblas-dev liblapack-dev libfreetype6-dev libpng-dev libtiff5-dev libjpeg-dev libfontconfig1-dev libcurl4-openssl-dev libharfbuzz-dev libfribidi-dev 
# install dependencies

$ rstudio & 
# launch RStudio

> install.packages("quantmod")

# which installs curl, TTR (Technical Trading Rule), xts (eXtensible Time Series), zoo (S3 Infrastructure for Regular and Irregular Time Series), quantmod (Quantitative Financial Modelling Framework)

> library('quantmod') 
> aapl = getSymbols('AAPL', auto.assign=FALSE)
> aapl = aapl["2022:2023"] 
> plot(aapl$AAPL.Adjusted)

```

### Install R from GitHub

https://cran.r-project.org/web/packages/githubinstall/vignettes/githubinstall.html

```
> install.packages("textshaping")
> install.packages("devtools")

> library("devtools")
> install_github("wgong/techchart")
```

#### Issues
```
ERROR: dependencies ‘deldir’, ‘RcppEigen’ are not available for package ‘interp’
FIX: $ sudo apt-get install gfortran
     > install.packages("deldir")

     > install.packages("RcppEigen")
ERROR: 
/usr/bin/ld: cannot find -llapack: No such file or directory
/usr/bin/ld: cannot find -lblas: No such file or directory
FIX: 
https://askubuntu.com/questions/623578/installing-blas-and-lapack-packages
$ sudo apt-get install libblas-dev liblapack-dev

ERROR: dependency ‘interp’ is not available for package ‘latticeExtra’
ERROR: dependency ‘latticeExtra’ is not available for package ‘Hmisc’
ERROR: dependency ‘Hmisc’ is not available for package ‘techchart’
FIX:
> install.packages(c('latticeExtra', 'Hmisc'))
```
### Learn R

#### Courses
- https://www.pluralsight.com/courses/programming-with-r

#### Tips and Tricks
The easiest way to resolve this problem is to install a binary, e.g. with https://packagemanager.rstudio.com/client/#/. Otherwise, you can use pak::pkg_system_requirements() to get an up-to-date list of system deps.