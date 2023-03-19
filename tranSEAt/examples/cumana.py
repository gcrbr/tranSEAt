import tranSEAt

stop = input('* Inserisci la tua fermata: ')
trains = tranSEAt.cumana.getOnlineArrivals(tranSEAt.cumana.getStopByName(stop))
for train in trains:
    print(f'> Cumana [{train.extra_info["train_number"]}] per {train.transport} tra {train.minutes} minuti')