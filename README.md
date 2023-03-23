# tranSEAt
![python 3.x](https://img.shields.io/static/v1?label=python&message=3.x&color=blue)

![tranSEAt logo](https://github.com/gcrbr/tranSEAt/blob/main/transeat.jpg?raw=true)

A python package to get arrival times of buses and trains in the metropolitan city of Naples.

## Installation
```
python3 setup.py install
```

## Features
- Calculate arrival times of trains based on public data (frequency, speed, etc.)
- Obtain live arrival times of trains/buses from companies' API
- Draw maps of supported rail lines by using [mplleaflet](https://github.com/jwass/mplleaflet)

## Featured means of transport
### ANM
| Transport | Available | Live arrival times | Calculated arrival times* |
| - | - | - | - |
| [Linea 1](https://www.anm.it/index.php?Itemid=98&id=71&option=com_content&task=view) | &check; | | &check; |
| [Bus](https://www.anm.it/index.php?option=com_content&task=view&id=1308&Itemid=260) | &check; | &check; | |
| [Funicolare centrale](https://www.anm.it/index.php?option=com_content&task=view&id=81&Itemid=383) | &check; | | &check; |
| [Funicolare di Montesanto](https://www.anm.it/index.php?option=com_content&task=view&id=83&Itemid=386) | &check; | | &check; |
| [Funicolare di Mergellina](https://www.anm.it/index.php?option=com_content&task=view&id=84&Itemid=384) | &check; | | &check; |
| [Funicolare di Chiaia](https://www.anm.it/index.php?option=com_content&task=view&id=82&Itemid=385) | | | |

### EAV
| Transport | Available | Live arrival times | Calculated arrival times* |
| - | - | - | - |
| [Cumana](https://www.eavsrl.it/web/orari-linee-ferroviarie) | &check; | &check; | &check; |
| [Circumflegrea](https://www.eavsrl.it/web/orari-linee-ferroviarie) | &check; | &check; | &check; |
| [Linea Arcobaleno/Metrocampania NordEst](https://www.eavsrl.it/web/orari-linee-ferroviarie) | &check; | &check; | &check; |
| [Circumvesuviana](https://www.eavsrl.it/web/orari-linee-ferroviarie) | | | |

### Trenitalia
| Transport | Available | Live arrival times | Calculated arrival times* |
| - | - | - | - |
| [Linea 2](https://www.trenitalia.com/it/treni_regionali/campania/metro_napoli.html) | &check; | &check; | &check; |

\*: Many of those rail lines are so f\*\*\*ed up that calculated times tend to be inaccurate most of the times

## Notes
I am not affiliated in any way with any of the companies mentioned in this project.

---
mplleaflet is broken, you can either [fix it manually](https://github.com/jwass/mplleaflet/issues/80) or run the command below

```bash
sed -i '' 's/axis._gridOnMajor/axis._major_tick_kw['gridOn']/' `python3 -c "print([os:=__import__('os'),os.path.join(os.path.dirname(__import__('mplleaflet').__file__), 'mplexporter/utils.py')][1])"`
```
