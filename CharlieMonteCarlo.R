#!/usr/bin/env Rscript
set.seed(2015)
subgames   <- 1000
supergames <- 10000 # maximum games is supergames*subgames
cases      <- 100000 
gain     <- function(x, y=9){ ifelse(y<9, y, y + 2^-ceiling(log(x,2)) -9) }
position <- matrix(rep(NA,(subgames+1) * cases), nrow=cases)
position[, 1] <- 250 # start with 100
for (r in 1:supergames){
    subcases <- nrow(position)
    udata <- matrix( runif(subgames * subcases ), nrow=subcases )
    for (n in 1:subgames ){ position[, n+1] <- gain(udata[,n], position[,n]) } 
    position[, 1] <- position[, subgames+1]     # ready to restart 
    position <- position[position[,1] >= 10, ] # remove lost games
    }
nrow(position)/cases
