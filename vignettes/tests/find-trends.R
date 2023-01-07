spx <- quantmod::getSymbols("^GSPC", auto.assign = FALSE)
spx <- spx["2021-12-01::2023-01-01"]

cpts <- techchart::find.major.trends(spx)

summary(cpts)

# Ctrl-Shift-C: add block comments
# change points:
#   [1]  74 108
# segments length summary:
#   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
# 34.0    54.0    74.0    91.0   119.5   165.0 
# segments returns summary:
#   -0.3113645 -0.5020528 -0.05242788
# segments offset summary:
#   0 0.07892437 -0.05103378


quantmod::chart_Series(spx)
quantmod::add_TA(cpts$segments[[1]],on=1,lty=3, col="red")
quantmod::add_TA(cpts$segments[[2]],on=1,lty=3, col="red")
quantmod::add_TA(cpts$segments[[3]],on=1,lty=3, col="red")
