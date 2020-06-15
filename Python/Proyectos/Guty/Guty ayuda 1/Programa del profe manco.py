#!/usr/bin/env python

import argparse
import random

def monteCarlo(N):
  Ncirculo = 0
  for i in range(N):
    x  = random.random()
    y  = random.random()
    if x*x + y*y < 1:
      Ncirculo = Ncirculo + 1
  pi =  4.0*Ncirculo/N
  print("monteCarlo")
  print(pi)
  return

def monteCarloPartial(N):
  Ncirculo = 0
  for i in range(N):
    x  = random.random()
    y  = random.random()
    if x*x + y*y < 1:
      Ncirculo = Ncirculo + 1
    pi =  4.0*Ncirculo/(i+1)
    print(pi)
  return

def monteCarloPlot(N, partial):
  Ncirculo = 0
  pi = []
  for i in range(N):
    x  = random.random()
    y  = random.random()
    if x*x + y*y < 1:
      Ncirculo = Ncirculo + 1
    pi.append(4.0*Ncirculo/(i+1))
    if partial:
      print(pi[-1])
  import matplotlib.pyplot as plt
  plt.plot(pi, 'ro-')
  plt.show()
  return
  

parser = argparse.ArgumentParser(description='Calular Pi por Monte Carlo.')
parser.add_argument('N', type=int, help='numero de iteraciones de MC ')
parser.add_argument('--partial', action='store_true', help='print partial results')
parser.add_argument('--plot', action='store_true', help='plot partial results')
args = parser.parse_args()

N = args.N

if args.plot:
  monteCarloPlot(N, args.partial)
  
elif args.partial:
  monteCarloPartial(N)
  
else:
  monteCarlo(N)