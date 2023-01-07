# install_github("wgong/techchart")
getwd()

library(quantmod)
spx <- getSymbols("^GSPC", auto.assign = FALSE)
spx <- spx["2021::2023"]
imppts <- techchart::find.imppoints(spx,2)
x <- print(imppts)
impptswrite.csv(x, file="~/projects/wgong/techchart/vignettes/tests/imppoints.csv")

chart_Series(spx)
points(as.numeric(imppts$maxima$pos),as.numeric(imppts$maxima$value),bg="green",pch=24,cex=1.25)
points(as.numeric(imppts$minima$pos),as.numeric(imppts$minima$value),bg="red",pch=25,cex=1.25)
