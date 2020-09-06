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
print ("\nall picture your download on where you place this script and in cache folder");

if check.status_code == 200:
  
  print("1.search\n2.about\n3.exit");
  select = input ("select menu :");
  
  def page (link):
    web_page = scrape.get(link);
    soup = BeautifulSoup(web_page.content,"html.parser");
    index=[];
    ul = soup.ul;
    div = soup.find_all("div")[7];
    if div.text == "Matching data could not be found":
      print(div.text);
      raise SystemExit;
    elif ul == None:
      print("server time out,please wait 1 minutes");
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
  
  if int(select) == 1:
    name= input("keyword:").replace(" ","+");
    mencari = link_web+"search/keyword/"+name;
    new_page = page(mencari);
    new_choosy = choosy(new_page);
    download(new_page,new_choosy);
  elif int(select) == 2:
    print("script by Novaldy");
    print("v1.7");
  elif int(select) == 3:
    raise SystemExit;
  else:
    print("tidak terdapat pada menu");
else:
  print("please use vpn "+str(check.status_code));
