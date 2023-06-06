import os.path

print('salut, entres ton pseudo') #on suppose que l'inscription est déja faite (sinon on peut aussi faire un module pour s'inscrire plus tard)
a=input()       #pas ed mdp pour l'instant
pseudo=str(a)
with open(pseudo+'.txt','r') as moi:
    content = moi.readlines()
password=str(content[0])
password=password[:len(password)-1]
a=''
while a!=(password):
    print('entres ton mot de passe :')
    a=input()
    a=str(a)

while True :

    solde=content[1][:len(content[1])-1]
    level=content[2][:len(content[2])-1]
    print()
    print("Tu as "+solde+" gold dans ton solde.")
    print("Tu es niveau "+level)
    print('que veux tu faire ?')
    print('1 : creer ta pool')
    print('2 : ajouter des personnes a une pool qui t appartiens')
    print('3 : supprimer une pool qui t appartient')
    print('4 : miser dans une pool')
    print('5 : update tes identifiants')
    print('6 : acceder a tes invitations')

    a=input()
    a=int(a)

    if a==5:
        print('quel est ton niveau ?')
        b=input()
        b=str(b)
        content[2]=b
    elif a==1:
        if content[3]=='1':
            print("deja au max de pool")
        else:
            print('quel est le niveau de la pool que tu veux creer ?')
            b=input()
            if b>level:
                print("le niveau dune pool doit etre inferieur ou egal a ton niveau")
            else:
                i=0
                while os.path.isfile("pool"+str(b)+"_"+str(i)+".txt") is True:
                    i=i+1
                with open("pool"+str(b)+"_"+str(i)+".txt",'w') as f:
                    f.write(b+'\n')
                    f.write('0\n')
                    f.write('1\n')                
                    f.write(content[0][:len(content[0])-1])
                content[3]=str(int(content[3])+1)
                content[4]=content[4][:len(content[4])-1]+"pool"+str(b)+"_"+str(i)+".txt \n"
                with open(pseudo+'.txt','w') as moi:
                    moi.writelines(content)
                print("tu as cree la pool : "+"pool"+str(b)+"_"+str(i)+".txt")
    elif a==2:
        list_pool=content[4].split()
        print('Tu as les pools : '+str(list_pool))
        print('selectionnes une pool parmis celles suivantes :')
        k=0
        for i in list_pool:
            print(str(k)+' : '+list_pool[k])
            k=k+1
        id=input()
        id=int(id)
        test=False
        while test==False:
            print('entres le pseudo de la personne que tu veux ajouter, sans se tromper : ', end='')
            invite=input()
            invite=str(invite)
            test=os.path.isfile(invite+".txt") #ajouter un vérificateur pour voir si la personne n'est pas deja dans la pool
        with open(invite+'.txt','r') as target:
            with open(list_pool[id],'r') as invite_pool:
                pool_content=invite_pool.readlines()
            invite_content=target.readlines()
        with open(invite+'.txt','w') as target:
            invite_content[5]=invite_content[5][:len(invite_content[5])-1]+' '+content[0][:len(content[0])-1]+'-'+pool_content[0][:len(pool_content[0])-1]+'-'+list_pool[id]+' \n' #on ajoute owner_niveau_idpool
            target.writelines(invite_content)
        print('done bitches')
    elif a==6:
        ligne=content[5][:len(content[5])-1]
        ligne=ligne.split()
        print(ligne)
        print('Voici les differentes invitations que tu as recu. Selectionnes l\'invitation que tu veux accepter')
        k=1
        print('0 | retour')
        for i in ligne:
            i=i.split('-')
            print(str(k)+' | proprietaire : '+i[0]+' ; niveau : '+i[1])
            k=k+1
        choix=input()
        if choix==0:
            break
        else :
            print(ligne)
            L=ligne[int(choix)-1].split('-') #ecrire à la suite de la ligne 4 de la pool L[2] le nom du participant
            print
            with open(L[2],'r') as target:
                lignes=target.readlines()
            lignes[3]=lignes[3]+' '+pseudo
            print(lignes[3])
            print('')
            print(pseudo)
            with open(L[2],'w') as target:
                target.writelines(lignes)
            print('l\'invitation est acceptee')