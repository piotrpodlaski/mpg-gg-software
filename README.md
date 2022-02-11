# Intro
This repository contains sources of ucLinux and u-boot with Smartfusion2 BSP. Bare ucLinux/u-boot sources were downloaded from [Emcraft](https://www.emcraft.com/component/jdownloads/view.download/57/826), with supplementary cross-compiler and developer tools from [Sourcery](https://sourcery.mentor.com/GNUToolchain/package6503/public/arm-uclinuxeabi/arm-2010q1-189-arm-uclinuxeabi-i686-pc-linux-gnu.tar.bz2).
# Compilation
A nice description of how to compile u-boot and ucLinux can be found [here](https://www.emcraft.com/docs/linux-cortexm-um-1.14.3.pdf). Thos section contains only extract.
## Environment setup
First we have to set up the ARM cross compiling environment. All the tools to be run are 32-bit, so we need compatibility packages.

On Ubuntu install required packages by running:
```
sudo apt install lib32ncurses5 lib32z1
```
Next, activate the environment by running:
```
source ACTIVATE.sh
```
## u-boot
To compile u-boot go too its directory:
```
cd u-boot
```
then, configure build for our target board:
```
make m2s-fg484-som_config
```
and finally compile:
```
make u-boot.hex
```
The resulting `u-boot.hex` file can be later embedded into Liber design as eNVM flash initialisation.

## ucLinux
To compile ucLinux project (for the moment sample project, will be updated) go to project directory (w.r.t. top repo direcotry):
```
cd projects/networking
```
and then run `make` to build the project. It will result in creation of linux image `networking.uImage` that can be loaded into the boars's flash, as described [here](https://www.emcraft.com/som/m2s-fg484/configuring-m2s-sk).

