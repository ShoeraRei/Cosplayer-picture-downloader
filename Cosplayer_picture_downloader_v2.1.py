import requests;
import cfscrape;
from bs4 import BeautifulSoup;
import os;

link_web = "https://hentai-cosplays.com/";
scrape = cfscrape.create_scraper();
check = scrape.get(link_web)

cache = os.path.join(".","cache");
if not os.path.exists(cache):
 os.mkdir(cache);

if check.status_code == 200:
  print ("\nall picture your download on where you place this script and in cache folder");
  print("1.search\n2.ranking\n3.about\n4.exit");
  select = input ("select menu :");
  
  def page (link):
    web_page = scrape.get(link);
    soup = BeautifulSoup(web_page.content,"html.parser");
    index=[];
    ul = soup.ul;
    div = soup.find_all("div")[7];
    if div.text == "Matching data could not be found":
      print(div.text);
      exit = input ("\npress enter for exit")
      raise SystemExit;
    elif ul == None:
      print("server time out,please wait 1 minutes");
      exit = input ("\npress enter for exit")
      raise SystemExit;
    else:  
      hr = ul.find_all("a");
      for hre in hr:
        href = hre.get("href");
        index.append(href);
      i=0;
      a=0;
      b=2-1;
      while i < len(index) :
        if (index[a]==index[b]):
          index.remove(index[b]);
        i += 1;
        a += 1;
        b += 1;
      c=0;
      count =len(index[c]);
      for idx in index :
        edit_string = index[c][7:count];
        print("\n"+str(c)+" . "+edit_string.replace("/",""))
        if (c < len(index)):
          c+=1
    return index;
  
  def choosy (idx):
    roster = input ("\nenter number your select :");
    new_number = roster;
    result = "https://hentai-cosplays.com"+idx[int(roster)]+"attachment/1/";
    new_scrape = scrape.get(result);
    new_soup = BeautifulSoup(new_scrape.content,"html.parser");
    title = new_soup.title.text;
    long_title = len(title)-17;
    string_title = title;
    print("\n"+string_title[0:long_title]);
    first_number = long_title-3;
    picture_number = string_title[first_number:long_title];
    print("\ntotal picture "+picture_number);
    
    return roster;
    
  def download (list_index,digit):
    new_link = "https://hentai-cosplays.com"+list_index[int(digit)];
    download_scrape = scrape.get(new_link);
    download_soup = BeautifulSoup(download_scrape.content,"html.parser");
    img = download_soup.find_all("img");
    
    k = True;
    l = 0;
    #2216917
    take_link = "";
    while k :
      src = img[l].get("src");
      if src[0:5] == "https":
        take_link = src;
        k= False;
      l += 1;
    
    new_count = int(input("how much picture you want ? :"));
    
    string_len = len(list_index[int(digit)]);
    folder = os.path.join(".","cache",list_index[int(digit)][7:string_len]);
    if not os.path.exists(folder):
      os.mkdir(folder);
    
    z = 0;
    x = 1;
    while new_count > z:
      translate = str(x);
      image_link = take_link[0:len(take_link)-12]+"/"+translate+".jpg";
      join_image_link = image_link;
      image_scrape = scrape.get(join_image_link);
      path = folder+translate+".jpg";
      with open (path ,"wb")as file : file.write(image_scrape.content);
      new_count -= 1;
      x += 1;
      print("picture "+translate+" .download complete");
    print("file location"+folder);
    exit = input ("\npress enter for exit")
  
  if int(select) == 1:
    name= input("keyword:").replace(" ","+");
    mencari = link_web+"search/keyword/"+name;
    if name == "":
      w = True;
      e = 1;
      while w :
        if e < 12429:
          r = link_web+"search/page/"+str(e)+"/";
          new_cosplay = page(r);
          next_cosplay = input("\nmove to next page ? [next/no]: ").lower();
          if next_cosplay == "next":
            e += 1;
          elif next_cosplay == "no":
            w = False;
          else:
            print("you can only choose \"next/no\"");
            raise SystemExit;
      new_choosy_cosplay = choosy(new_cosplay);
      new_cosplay_downlod = download(new_cosplay,new_choosy_cosplay);
    else:      
      new_page = page(mencari);
      new_choosy = choosy(new_page);
      download(new_page,new_choosy);
  elif int(select) == 2:
    ranking = link_web+"ranking/";
    q = True;
    o = 1;
    while q :
      if o < 2568:
        p = "page/"+str(o)+"/";
        ranking_page = page(ranking+p);
        page_next = input("\nmove to next page ? [next/no]: ").lower();
        if page_next == "next":
          o += 1;
        elif page_next == "no":
          q = False;
        else:
          print("you can only choose \"next/no\"");
          raise SystemExit;
          
    ranking_choosy = choosy(ranking_page);
    ranking_download = download(ranking_page,ranking_choosy);
  elif int(select) == 3:
    print("script by ShoeraRei");
    print("v2.1")
    exit = input ("\npress enter for exit")
  elif int(select) == 4:
    raise SystemExit;
  else:
    print("tidak terdapat pada menu");
    exit = input ("\npress enter for exit")
else:
  print("please use vpn or change vpn "+str(check.status_code));
  exit = input ("\npress enter for exit")