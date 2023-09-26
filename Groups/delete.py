import json

# List of LinkedIn URLs separated by commas
input_urls = "http://marketojbwagqnwx.onion, http://g5sbltooh2okkcb2.onion, http://fvki3hj7uxuirxpeop6chgqoczanmebutznt2mkzy6waov6w456vjuid.onion, http://jvdamsif53dqjycuozlaye2s47p7xij4x6hzwzwhzrqmv36gkyzohhqd.onion, http://xqkz2rmrqkeqf6sjbrb47jfwnqxcd4o2zvaxxzrpbh2piknms37rw2ad.onion, http://x2miyuiwpib2imjr5ykyjngdu7v6vprkkhjltrk4qafymtawey4qzwid.onion, http://nbzzb6sa6xuura2z.onion, http://rbvuetuneohce3ouxjlbxtimyyxokb4btncxjbo44fbgxqy7tskinwad.onion, http://4qbxi3i2oqmyzxsjg4fwe4aly3xkped52gq5orp6efpkeskvchqe27id.onion, http://lorenzmlwpzgxq736jzseuterytjueszsvznuibanxomlpkyxk6ksoyd.onion, http://zqaflhty5hyziovsxgqvj2mrz5e5rs6oqxzb54zolccfnvtn5w2johad.onion, http://yq43odyrmzqvyezdindg2tokgogf3pn6bcdtvgczpz5a74tdxjbtk2yd.onion, http://oyarbnujct53bizjguvolxou3rmuda2vr72osyexngbdkhqebwrzsnad.onion, http://lockbitaptstzf3er2lz6ku3xuifafq2yh5lmiqj5ncur6rtlmkteiqd.onion, http://lockbitaptq7ephv2oigdncfhtwhpqgwmqojnxqdyhprxxfpcllqdxad.onion, http://hiveleakdbtnp76ulyhi52eag6c6tyc3xw7ez7iqy6wc34gd2nekazyd.onion, http://hivecust6vhekztbqgdnkks64ucehqacge3dij3gyrrpdp57zoq3ooqd.onion, http://hiveapi4nyabjdfz2hxdsr7otrcv6zq6m4rk5i2w7j64lrtny4b7vjad.onion, http://3kp6j22pz3zkv76yutctosa6djpj4yib2icvdqxucdaxxedumhqicpad.onion, http://avosqxh72b5ia23dl5fgwcpndkctuzqvh2iefk5imp3pi5gfhel5klad.onion, http://avosjon4pfh3y7ew3jdwz6ofw7lljcxlbk7hcxxmnxlh5kvf2akcqjad.onion, http://griefcameifmv4hfr3auozmovz5yi6m3h3dwbuqw7baomfxoxz4qteid.onion, http://avaddongun7rngel.onion, http://4hzyuotli6maqa4u.onion, http://vsociethok6sbprvevl4dlwbqrzyhxcxaqpvcqt5belwvsuxaxsutyad.onion, http://ecdmr42a34qovoph557zotkfvth4fsz56twvwgiylstjup4r5bpc4oad.onion, http://wmp2rvrkecyx72i3x7ejhyd3yr6fn5uqo7wfus7cz7qnwr6uzhcbrwad.onion, http://ssq4zimieeanazkzc5ld4v5hdibi2nzwzdibfh5n5w4pw5mcik76lzyd.onion, http://ml3mjpuhnmse4kjij7ggupenw34755y4uj7t742qf7jg5impt5ulhkid.onion, http://xingnewj6m4qytljhfwemngm7r7rogrindbq7wrfeepejgxc3bwci7qd.onion, http://darksidc3iux462n6yunevoag52ntvwp6wulaz3zirkmh4cnz6hhj7id.onion, http://rgleaktxuey67yrgspmhvtnrqtgogur35lwdrup4d3igtbm3pupc4lyd.onion, http://p6o7m73ujalhgkiv.onion, http://ekbgzchl6x2ias37.onion, http://santat7kpllt6iyvqbr7q4amdv6dzrh6paatvyrzl7ry3zm72zigf4ad.onion, http://rnfdsgm6wb6j6su5txkekw4u4y47kp2eatvu7d6xhyn5cs4lt4pdrqqd.onion, http://hpoo4dosa3x4ognfxpqcrjwnsigvslm7kv6hvmhh2yqczaxy3j6qnwad.onion, http://dnpscnbaix6nkwvystl3yxglz7nteicqrou3t75tpcc5532cztc46qyd.onion, http://aplebzu47wgazapdqks6vrcv6zcnjppkbxbr6wketf56nf6aq2nmyoyd.onion, http://blogxxu75w63ujqarv476otld7cyjkq4yoswzt4ijadkjwvg3vrvd5yd.onion, http://ransomocmou6mnbquqz44ewosbkjk3o5qjsl3orawojexfook2j7esad.onion, http://wobpitin77vdsdiswr43duntv6eqw4rvphedutpaxycjdie6gg3binad.onion, http://sushlnty2j7qdzy64qnvyb6ajkwg7resd3p6agc2widnawodtcedgjid.onion, http://continewsnv5otx5kaoje7krkto2qbu3gtqef22mnr7eaxw3y6ncz3ad.onion, http://continews.click, http://continews.bz, http://pysa2bitc5ldeyfak4seeruqymqs4sj5wt5qkcq7aoyg4h2acqieywad.onion, http://hxt254aygrsziejn.onion, http://xfr3txoorcyy7tikjgj5dk3rvo3vsrpyaxnclyohkbfp3h277ap4tiad.onion, http://mountnewsokhwilx.onion, http://nq4zyac4ukl4tykmidbzgdlvaboqeqsemkp4t35bzvjeve6zm2lqcjid.onion, http://rnsm777cdsjrsdlbs4v5qoeppu3px6sb2igmh53jzrx7ipcrbjz5b2ad.onion, http://cuba4mp6ximo2zlo.onion, http://cuba4ikm4jakjgmkezytyawtdgr2xymvy6nvzgw5cglswg3si76icnqd.onion, http://pay2key2zkg7arp3kv3cuugdaqwuesifnbofun4j6yjdw5ry7zw2asid.onion, http://anewset3pcya3xvk73hj7yunuamutxxsm5sohkdi32blhmql55tvgqad.onion, http://wm6mbuzipviusuc42kcggzkdpbhuv45sn7olyamy6mcqqked3waslbqd.onion, http://bl4cktorpms2gybrcyt52aakcxt6yn37byb65uama5cimhifcscnqkid.onion, http://ft4zr2jzlqoyob7yg4fcpwyt37hox3ajajqnfkdvbfrkjioyunmqnpad.onion, http://54rdhzjzc4ids4u4wata4zr4ywfon5wpz2ml4q3avelgadpvmdal2vqd.onion, http://aby6efzmp7jzbwgidgqc6ghxi2vwpo6d7eaood5xuoxutrfofsmzcjqd.onion, http://darklmmmfuonklpy6s3tmvk5mrcdi7iapaw6eka45esmoryiiuug6aid.onion, http://darkleakyqmv62eweqwy4dnhaijg4m4dkburo73pzuqfdumcntqdokyd.onion, http://promethw27cbrcot.onion, http://blackmax7su6mbwtcyo3xwtpfxpm356jjqrs34y4crcytpw7mifuedyd.onion, http://vbmisqjshn4yblehk2vbnil53tlqklxsdaztgphcilto3vdj4geao5qd.onion, http://ws3dh6av66sjbxxkjpw5ao3wqzmtejnkzheswm4dz5rrwvular7xvkqd.onion, http://kwvhrdibgmmpkhkidrby4mccwqpds5za6uo2thcw5gz75qncv7rbhyad.onion, http://mhdehvkomeabau7gsetnsrhkfign4jgnx3wajth5yb5h6kvzbd72wlqd.onion, http://l5cjga2ksw6rxumu5l4xxn3cmahhi2irkbwg3amx6ajroyfmfgpfllid.onion, http://avos2fuj6olp6x36.onion, http://6iaj3efye3q62xjgfxyegrufhewxew7yt4scxjd45tlfafyja6q4ctqd.onion, http://f5uzduboq4fa2xkjloprmctk7ve3dm46ff7aniis66cbekakvksxgeqd.onion, http://dlyo7r3n4qy5fzv4645nddjwarj7wjdd6wzckomcyc7akskkxp4glcad.onion, http://fl3xpz5bmgzxy4fmebhgsbycgnz24uosp3u4g33oiln627qq3gyw37ad.onion, http://ce6roic2ykdjunyzazsxmjpz5wsar4pflpoqzntyww5c2eskcp7dq4yd.onion, http://jbeg2dct2zhku6c2vwnpxtm2psnjo2xnqvvpoiiwr5hxnc6wrp3uhnad.onion, http://mmeeiix2ejdwkmseycljetmpiwebdvgjts75c63camjofn2cjdoulzqd.onion, http://obzuqvr5424kkc4unbq2p2i67ny3zngce3tbdr37nicjqesgqcgomfqd.onion, http://nclen75pwlgebpxpsqhlcnxsmdvpyrr7ogz36ehhatfmkvakeyden6ad.onion, http://544corkfh5hwhtn4.onion, http://bonacifryrxr4siz6ptvokuihdzmjzpveruklxumflz5thmkgauty2qd.onion, http://d57uremugxjrafyg.onion, http://veqlxhq7ub5qze3qy56zx2cig2e6tzsgxdspkubwbayqije6oatma6id.onion, http://dg5fyig37abmivryrxlordrczn6d6r5wzcfe2msuo5mbbu2exnu46fid.onion, http://7iulpt5i6whht6zo2r52f7vptxtjxs3vfcdxxazllikrtqpupn4epnqd.onion, http://ixltdyumdlthrtgx.onion, http://3r6n77mpe737w4sbxxxrpc5phbluv6xhtdl5ujpnlvmck5tc7blq2rqd.onion, http://r6d636w47ncnaukrpvlhmtdbvbeltc6enfcuuow3jclpmyga7cz374qd.onion, http://3nvzqyo6l4wkrzumzu5aod7zbosq4ipgf7ifgj3hsvbcr5vcasordvqd.onion, http://lockbitkodidilol.onion, http://xembshruusobgbvxg4tcjs3jpdnks6xrr6nbokfxadcnlc53yxir22ad.onion, http://5s4ixqul2enwxrqv.onion, http://n3twormruynhn3oetmxvasum2miix2jgg56xskdoyihra4wthvlgyeyd.onion, http://zjoxyw5mkacojk5ptn2iprkivg5clow72mjkyk5ttubzxprjjnwapkad.onion, http://5mvifa3xq5m7sou3xzaajfz7h6eserp5fnkwotohns5pgbb5oxty3zad.onion, http://msaoyrayohnp32tcgwcanhjouetb5k54aekgnwg7dcvtgtecpumrxpqd.onion, http://gvka2m4qt5fod2fltkjmdk4gxh5oxemhpgmnmtjptms6fkgfzdd62tad.onion, http://37rckgo66iydpvgpwve7b2el5q2zhjw4tv4lmyewufnpx4lhkekxkoqd.onion, http://vfokxcdzjbpehgit223vzdzwte47l3zcqtafj34qrr26htjo4uf3obid.onion, http://746pbrxl7acvrlhzshosye3b3udk4plurpxt2pp27pojfhkkaooqiiqd.onion, http://wj3b2wtj7u2bzup75tzhnso56bin6bnvsxcbwbfcuvzpc4vcixbywlid.onion, http://spookuhvfyxzph54ikjfwf2mwmxt572krpom7reyayrmxbkizbvkpaid.onion, http://wavbeudogz6byhnardd2lkp2jafims3j7tj6k6qnywchn2csngvtffqd.onion, http://rampjcdlqvgkoz5oywutpo6ggl7g6tvddysustfl6qzhr5osr24xxqqd.onion, http://ramp4u5iz4xx75vmt6nk5xfrs5mrmtokzszqxhhkjqlk7pbwykaz7zid.onion, http://54bb47h5qu4k7l4d7v5ix3i6ak6elysn3net4by4ihmvrhu7cvbskoqd.onion, http://quantum445bh3gzuyilxdzs5xdepf3b7lkcupswvkryf3n7hgzpxebid.onion, http://22rnyep2aa2exx3fdm26p4onwjfmhciodb55v5l3w4iny7e5bxpg3yad.onion, http://qd7pcafncosqfqu3ha6fcx4h6sr7tzwagzpcdcnytiw3b6varaeqv5yd.onion, http://medusaxko7jxtrojdkxo66j7ck4q5tgktf7uqsqyfry4ebnxlcbkccyd.onion, http://hl66646wtlp2naoqnhattngigjp5palgqmbwixepcjyq5i534acgqyad.onion, http://midasbkic5eyfox4dhnijkzc7v7e4hpmsb2qgux7diqbpna4up4rtdad.onion, http://leaksv7sroztl377bbohzl42i3ddlfsxopcb6355zc7olzigedm5agad.onion, http://mosesstaffm7hptp.onion, http://z6mikrtphid5fmn52nbcbg25tj57sowlm3oc25g563yvsfmygkcxqbyd.onion, http://teo7aj5mfgzxyeme.onion, http://gamol6n6p2p4c3ad7gxmx3ur7wwdwlywebo2azv3vv5qlmjmole2zbyd.onion, http://tdoe2fiiamwkiadhx2a4dfq56ztlqhzl2vckgwmjtoanfaya4kqvvvyd.onion, http://darktorhvabc652txfc575oendhykqcllb7bh7jhhsjduocdlyzdbmqd.onion, http://t2tqvp4pctcr7vxhgz5yd5x4ino5tw7jzs3whbntxirhp32djhi7q3id.onion, http://babydovegkmhbontykziyq7qivwzy33mu4ukqefe4mqpiiwd3wibnjqd.onion, http://alphvmmm27o3abo3r2mlmjrpdmzle3rykajqc5xsj7j7ejksbpsa36ad.onion, http://2cuqgeerjdba2rhdiviezodpu3lc4qz2sjf4qin6f7std2evleqlzjid.onion, http://vqifktlreqpudvulhbzmc5gocbeawl67uvs2pttswemdorbnhaddohyd.onion, http://7k4yyskpz3rxq5nyokf6ztbpywzbjtdfanweup3skctcxopmt7tq7eid.onion, http://dreadytofatroptsdj6io7l3xptbet6onoyno2yv7jicoxknyazubrad.onion, http://giphvoitymatg4cv7bxqh5dz6sn6bfscywoat4qtslztkomf5lavrayd.onion, http://matmq3z3hiovia3voe2tix2x54sghc3tszj74xgdy4tqtypoycszqzqd.onion, http://gg5ryfgogainisskdvh4y373ap3b2mxafcibeh2lvq5x7fx76ygcosad.onion, http://u67aylig7i6l657wxmp274eoilaowhp3boljowa6bli63rxyzfzsbtyd.onion, http://cartelirsn5l54ehcbalyyqtfb3j7be2rpvf6ujayaf5qqmg3vlwiayd.onion, http://cartelraqonekult2cxbzzz2ukiff7v6cav3w373uuhenybgqulxm5id.onion, http://adminavf4cikzbv6mbbp7ujpwhygnn2t3egiz2pswldj32krrml42wyd.onion, http://chat5sqrnzqewampznybomgn4hf2m53tybkarxk4sfaktwt7oqpkcvyd.onion, http://zeonrefpbompx6rwdqa5hxgtp2cxgfmoymlli3azoanisze33pp3x3yd.onion, http://gcbejm2rcjftouqbxuhimj5oroouqcuxb2my4raxqa7efkz5bd5464id.onion, http://vbfqeh5nugm6r2u2qvghsdxm3fotf5wbxb5ltv6vw77vus5frdpuaiid.onion, http://3slz4povugieoi3tw7sblxoowxhbzxeju427cffsst5fo2tizepwatid.onion, http://leaktheanalyst.fireeye62c3da3fnosymmmcqcty7rl7cjucpbkzaz275a4qs5fgkzhad.onion, http://ranionv3j2o7wrn3um6de33eccbchhg32mkgnnoi72enkpp7jc25h3ad.onion, http://nalr2uqsave7y2r235am5jsfiklfjh5h4jc5nztu3rzvmhklwt5j6kid.onion, http://stniiomyjliimcgkvdszvgen3eaaoz55hreqqx6o77yvmpwt7gklffqd.onion, http://aazsbsgya565vlu2c6bzy6yfiebkcbtvvcytvolt33s77xypi7nypxyd.onion, http://bastad5huzwkepdixedg2gekg7jk22ato24zyllp6lnjx7wdtyctgvyd.onion, http://mrdxtxy6vqeqbmb4rvbvueh2kukb3e3mhu3wdothqn7242gztxyzycid.onion, http://dfpc7yvle5kxmgg6sbcp5ytggy3oeob676bjgwcwhyr2pwcrmbvoilqd.onion, http://xw7au5pnwtl6lozbsudkmyd32n6gnqdngitjdppybudan3x3pjgpmpid.onion, http://zohlm7ahjwegcedoz7lrdrti7bvpofymcayotp744qhx6gjmxbuo2yid.onion, http://rwiajgajdr4kzlnrj5zwebbukpcbrjhupjmk6gufxv6tg7myx34iocad.onion, http://crkfkmrh4qzbddfrl2axnkvjp5tgwx73d7lq4oycsfxc7pfgbfhtfiid.onion, http://wemo2ysyeq6km2nqhcrz63dkdhez3j25yw2nvn7xba2z4h7v7gyrfgid.onion, http://lockbitapt2d73krlbewgv27tquljgxr33xbwwsp6rkyieto7u4ncead.onion, http://lockbitapt2yfbt7lchxejug47kmqvqqxvvjpqkmevv4l3azl3gy6pyd.onion, http://lockbitapt34kvrip6xojylohhxrwsvpzdffgs5z4pbbsywnzsbdguqd.onion, http://lockbitapt5x4zkjbcqmz6frdhecqqgadevyiwqxukksspnlidyvd7qd.onion, http://lockbitapt6vx57t3eeqjofwgcglmutr3a35nygvokja5uuccip4ykyd.onion, http://lockbitapt72iw55njgnqpymggskg5yp75ry7rirtdg4m7i42artsbqd.onion, http://lockbitaptawjl6udhpd323uehekiyatj6ftcxmkwe5sezs4fqgpjpid.onion, http://lockbitaptbdiajqtplcrigzgdjprwugkkut63nbvy2d5r4w2agyekqd.onion, http://lockbitaptc2iq4atewz2ise62q63wfktyrl4qtwuk5qax262kgtzjqd.onion, http://lockbitapt72iw55njgnqpymggskg5yp75ry7rirtdg4m7i42artsbqd.onion, http://lockbitsupa7e3b4pkn4mgkgojrl5iqgx24clbzc4xm7i6jeetsia3qd.onion, http://lockbitsupdwon76nzykzblcplixwts4n4zoecugz2bxabtapqvmzqqd.onion, http://lockbitsupn2h6be2cnqpvncyhj4rgmnwn44633hnzzmtxdvjoqlp7yd.onion, http://lockbitsupo7vv5vcl3jxpsdviopwvasljqcstym6efhh6oze7c6xjad.onion, http://lockbitsupqfyacidr6upt6nhhyipujvaablubuevxj6xy3frthvr3yd.onion, http://lockbitsupt7nr3fa6e7xyb73lk6bw6rcneqhoyblniiabj4uwvzapqd.onion, http://lockbitsupuhswh4izvoucoxsbnotkmgq6durg7kficg6u33zfvq3oyd.onion, http://lockbitsupxcjntihbmat4rrh7ktowips2qzywh6zer5r3xafhviyhqd.onion, http://lockbitsupq3g62dni2f36snrdb4n5qzqvovbtkt5xffw3draxk6gwqd.onion, http://lockbitfile2tcudkcqqt2ve6btssyvqwlizbpv5vz337lslmhff2uad.onion, http://lockbitnotexk2vnf2q2zwjefsl3hjsnk4u74vq4chxrqpjclfydk4ad.onion, http://ccpyeuptrlatb2piua4ukhnhi7lrxgerrcrj4p2b5uhbzqm2xgdjaqid.onion, http://solidb2jco63vbhx4sfimnqmwhtdjk4jbbgq7a24cmzzkfse4rduxgid.onion, http://jukswsxbh3jsxuddvidrjdvwuohtsy4kxg2axbppiyclomt2qciyfoad.onion, http://lirncvjfmdhv6samxvvlohfqx7jklfxoxj7xn3fh7qeabs3taemdsdqd.onion, http://6yofnrq7evqrtz3tzi3dkbrdovtywd35lx3iqbc5dyh367nrdh4jgfyd.onion, http://omx5iqrdbsoitf3q4xexrqw5r5tfw7vp3vl3li3lfo7saabxazshnead.onion, http://3f7nxkjway3d223j27lyad7v5cgmyaifesycvmwq7i7cbs23lb6llryd.onion, http://blog2hkbm6gogpv2b3uytzi3bj5d5zmc4asbybumjkhuqhas355janyd.onion, http://bianlianlbc5an4kgnay3opdemgcryg2kpfcbgczopmm3dnbz3uaunad.onion, http://omegalock5zxwbhswbisc42o2q2i54vdulyvtqqbudqousisjgc7j7yd.onion, http://yeuajcizwytgmrntijhxphs6wn5txp2prs6rpndafbsapek3zd4ubcid.onion, http://lockbit7z2jwcskxpbokpemdxmltipntwlkmidcll2qirbu7ykg46eyd.onion, http://lockbit7z2mmiz3ryxafn5kapbvbbiywsxwovasfkgf5dqqp5kxlajad.onion, http://lockbit7z2og4jlsmdy7dzty3g42eu3gh2sx2b6ywtvhrjtss7li4fyd.onion, http://lockbit7z355oalq4hiy5p7de64l6rsqutwlvydqje56uvevcc57r6qd.onion, http://lockbit7z36ynytxwjzuoao46ck7b3753gpedary3qvuizn3iczhe4id.onion, http://lockbit7z37ntefjdbjextn6tmdkry4j546ejnru5cejeguitiopvhad.onion, http://lockbit7z3azdoxdpqxzliszutufbc2fldagztdu47xyucp25p4xtqad.onion, http://lockbit7z3ddvg5vuez2vznt73ljqgwx5tnuqaa2ye7lns742yiv2zyd.onion, http://lockbit7z3hv7ev5knxbrhsvv2mmu2rddwqizdz4vwfvxt5izrq6zqqd.onion, http://lockbit7z3ujnkhxwahhjduh5me2updvzxewhhc5qvk2snxezoi5drad.onion, http://lockbit7z4bsm63m3dagp5xglyacr4z4bwytkvkkwtn6enmuo5fi5iyd.onion, http://lockbit7z4cgxvictidwfxpuiov4scdw34nxotmbdjyxpkvkg34mykyd.onion, http://lockbit7z4k5zer5fbqi2vdq5sx2vuggatwyqvoodrkhubxftyrvncid.onion, http://lockbit7z4ndl6thsct34yd47jrzdkpnfg3acfvpacuccb45pnars2ad.onion, http://lockbit7z55tuwaflw2c7torcryobdvhkcgvivhflyndyvcrexafssad.onion, http://lockbit7z57mkicfkuq44j6yrpu5finwvjllczkkp2uvdedsdonjztyd.onion, http://lockbit7z5ehshj6gzpetw5kso3onts6ty7wrnneya5u4aj3vzkeoaqd.onion, http://lockbit7z5hwf6ywfuzipoa42tjlmal3x5suuccngsamsgklww2xgyqd.onion, http://lockbit7z5ltrhzv46lsg447o3cx2637dloc3qt4ugd3gr2xdkkkeayd.onion, http://lockbit7z6choojah4ipvdpzzfzxxchjbecnmtn4povk6ifdvx2dpnid.onion, http://lockbit7z6dqziutocr43onmvpth32njp4abfocfauk2belljjpobxyd.onion, http://lockbit7z6f3gu6rjvrysn5gjbsqj3hk3bvsg64ns6pjldqr2xhvhsyd.onion, http://lockbit7z6qinyhhmibvycu5kwmcvgrbpvtztkvvmdce5zwtucaeyrqd.onion, http://lockbit7z6rzyojiye437jp744d4uwtff7aq7df7gh2jvwqtv525c4yd.onion, http://232fwh5cea3ub6qguz3pynijxfzl2uj3c73nbrayipf3gq25vtq2r4qd.onion, http://7ukmkdtyxdkdivtjad57klqnd3kdsmq6tp45rrsxqnu76zzv3jvitlqd.onion, http://kf6x3mjeqljqxjznaw65jixin7dpcunfxbbakwuitizytcpzn4iy5bad.onion, http://7kstc545azxeahkduxmefgwqkrrhq3mzohkzqvrv7aekob7z3iwkqvyd.onion, http://qkbbaxiuqqcqb5nox4np4qjcniy2q6m7yeluvj7n5i5dn7pgpcwxwfid.onion, http://sbc2zv2qnz5vubwtx3aobfpkeao6l4igjegm3xx7tk5suqhjkp5jxtqd.onion, http://doq32rjiuomfghm5a4lyf3lwwakt2774tkv4ppsos6ueo5mhx7662gid.onion, http://ozsxj4hwxub7gio347ac7tyqqozvfioty37skqilzo2oqfs4cw2mgtyd.onion, http://kbsqoivihgdmwczmxkbovk7ss2dcynitwhhfu5yw725dboqo5kthfaad.onion, http://7ypnbv3snejqmgce4kbewwvym4cm5j6lkzf2hra2hyhtsvwjaxwipkyd.onion, http://4s4lnfeujzo67fy2jebz2dxskez2gsqj2jeb35m75ktufxensdicqxad.onion, http://mblogci3rudehaagbryjznltdp33ojwzkq6hn2pckvjq33rycmzczpid.onion, http://zj2ex44e2b2xi43m2txk4uwi3l55aglsarre7repw7rkfwpj54j46iqd.onion, http://z6vidveub2ypo3d3x7omsmcxqwxkkmvn5y3paoufyd2tt4bfbkg33kid.onion, http://dgnh6p5uq234zry7qx7bh73hj5ht3jqisgfet6s7j7uyas5i46xfdkyd.onion, http://royal2xthig3ou5hd7zsliqagy6yygk2cdelaxtni2fyad6dpmpxedid.onion, http://royal4ezp7xrbakkus3oofjw6gszrohpodmdnfbe5e4w3og5sm7vb3qd.onion, http://crptd5sv5bdz6hovrbkac6mnp3rt7zij62njsqwh5a6ldd3asxdd22qd.onion, http://wtyafjyhwqrgo4a45wdvvwhen3cx4euie73qvlhkhvlrexljoyuklaad.onion, http://relic5zqwemjnu4veilml6prgyedj6phs7de3udhicuq53z37klxm6qd.onion, http://k7kg3jqxang3wh7hnmaiokchk7qoebupfgoik6rha6mjpzwupwtj25yd.onion, http://mbrlkbtq5jonaqkurjwmxftytyn2ethqvbxfu4rgjbkkknndqwae6byd.onion, http://woqjumaahi662ka26jzxyx7fznbp4kg3bsjar4b52tqkxgm2pylcjlad.onion, http://unsafeipw6wbkzzmj7yqp7bz6j7ivzynggmwxsm6u2wwfmfqrxqrrhyd.onion, http://nevcorps5cvivjf6i2gm4uia7cxng5ploqny2rgrinctazjlnqr2yiyd.onion, http://nevbackvzwfu5yu3gszap77bg66koadds6eln37gxdhdk4jdsbkayrid.onion, http://nevaffcwswjosddmw55qhn4u4secw42wlppzvf26k5onrlxjevm6avad.onion, http://test.cuba4ikm4jakjgmkezytyawtdgr2xymvy6nvzgw5cglswg3si76icnqd.onion, http://contiuevxdgdhn3zl2kubpajtfgqq4ssj2ipv6ujw7fwhggev3rk6hqd.onion, http://z6wkgghtoawog5noty5nxulmmt2zs7c3yvwr22v4czbffdoly2kl4uad.onion, http://iw6v2p3cruy7tqfup3yl4dgt4pfibfa3ai4zgnu5df2q3hus3lm7c7ad.onion, http://cuba4ikm4jakjgmkezytyawtdgr2xymvy6nvzgw5cglswg3si76icnqd.onion, http://abrahamm32umasogaqojib3ey2w2nwoafffrguq43tsyke4s3fz3w4yd.onion, http://iw6v2p3cruy7tqfup3yl4dgt4pfibfa3ai4zgnu5df2q3hus3lm7c7ad.onion, http://santat7kpllt6iyvqbr7q4amdv6dzrh6paatvyrzl7ry3zm72zigf4ad.onion, http://z6vidveub2ypo3d3x7omsmcxqwxkkmvn5y3paoufyd2tt4bfbkg33kid.onion, http://ccpyeuptrlatb2piua4ukhnhi7lrxgerrcrj4p2b5uhbzqm2xgdjaqid.onion, http://stniiomyjliimcgkvdszvgen3eaaoz55hreqqx6o77yvmpwt7gklffqd.onion, http://abrahamm32umasogaqojib3ey2w2nwoafffrguq43tsyke4s3fz3w4yd.onion, http://alphvmmm27o3abo3r2mlmjrpdmzle3rykajqc5xsj7j7ejksbpsa36ad.onion, http://3kp6j22pz3zkv76yutctosa6djpj4yib2icvdqxucdaxxedumhqicpad.onion, http://anewset3pcya3xvk73hj7yunuamutxxsm5sohkdi32blhmql55tvgqad.onion, http://l5cjga2ksw6rxumu5l4xxn3cmahhi2irkbwg3amx6ajroyfmfgpfllid.onion, http://nmhdehvkomeabau7gsetnsrhkfign4jgnx3wajth5yb5h6kvzbd72wlqd.onion, http://avosqxh72b5ia23dl5fgwcpndkctuzqvh2iefk5imp3pi5gfhel5klad.onion, http://nq4zyac4ukl4tykmidbzgdlvaboqeqsemkp4t35bzvjeve6zm2lqcjid.onion, http://bianlianlbc5an4kgnay3opdemgcryg2kpfcbgczopmm3dnbz3uaunad.onion, http://stniiomyjliimcgkvdszvgen3eaaoz55hreqqx6o77yvmpwt7gklffqd.onion, http://ce6roic2ykdjunyzazsxmjpz5wsar4pflpoqzntyww5c2eskcp7dq4yd.onion, http://n6iaj3efye3q62xjgfxyegrufhewxew7yt4scxjd45tlfafyja6q4ctqd.onion, http://nf5uzduboq4fa2xkjloprmctk7ve3dm46ff7aniis66cbekakvksxgeqd.onion, http://ndlyo7r3n4qy5fzv4645nddjwarj7wjdd6wzckomcyc7akskkxp4glcad.onion, http://nfl3xpz5bmgzxy4fmebhgsbycgnz24uosp3u4g33oiln627qq3gyw37ad.onion, http://njbeg2dct2zhku6c2vwnpxtm2psnjo2xnqvvpoiiwr5hxnc6wrp3uhnad.onion, http://blackmax7su6mbwtcyo3xwtpfxpm356jjqrs34y4crcytpw7mifuedyd.onion, http://bl4cktorpms2gybrcyt52aakcxt6yn37byb65uama5cimhifcscnqkid.onion, http://bonacifryrxr4siz6ptvokuihdzmjzpveruklxumflz5thmkgauty2qd.onion, http://rwiajgajdr4kzlnrj5zwebbukpcbrjhupjmk6gufxv6tg7myx34iocad.onion, http://santat7kpllt6iyvqbr7q4amdv6dzrh6paatvyrzl7ry3zm72zigf4ad.onion, http://nekbgzchl6x2ias37.onion, http://continewsnv5otx5kaoje7krkto2qbu3gtqef22mnr7eaxw3y6ncz3ad.onion, http://z6mikrtphid5fmn52nbcbg25tj57sowlm3oc25g563yvsfmygkcxqbyd.onion, http://7k4yyskpz3rxq5nyokf6ztbpywzbjtdfanweup3skctcxopmt7tq7eid.onion, http://cuba4mp6ximo2zlo.onion, http://ncuba4ikm4jakjgmkezytyawtdgr2xymvy6nvzgw5cglswg3si76icnqd.onion, http://7ukmkdtyxdkdivtjad57klqnd3kdsmq6tp45rrsxqnu76zzv3jvitlqd.onion, http://wemo2ysyeq6km2nqhcrz63dkdhez3j25yw2nvn7xba2z4h7v7gyrfgid.onion, http://nwemo2ysyeq6km2nqhcrz63dkdhez3j25yw2nvn7xba2z4h7v7gyrfgid.onion, http://darklmmmfuonklpy6s3tmvk5mrcdi7iapaw6eka45esmoryiiuug6aid.onion, http://ndarkleakyqmv62eweqwy4dnhaijg4m4dkburo73pzuqfdumcntqdokyd.onion, http://woqjumaahi662ka26jzxyx7fznbp4kg3bsjar4b52tqkxgm2pylcjlad.onion, http://sbc2zv2qnz5vubwtx3aobfpkeao6l4igjegm3xx7tk5suqhjkp5jxtqd.onion, http://hpoo4dosa3x4ognfxpqcrjwnsigvslm7kv6hvmhh2yqczaxy3j6qnwad.onion, http://adminavf4cikzbv6mbbp7ujpwhygnn2t3egiz2pswldj32krrml42wyd.onion, http://h44jyyfomcbnnw5dha7zgwgkvpzbzbdyx2onu4fxaa5smxrgbjgq7had.onion, http://leaksv7sroztl377bbohzl42i3ddlfsxopcb6355zc7olzigedm5agad.onion, http://ransomocmou6mnbquqz44ewosbkjk3o5qjsl3orawojexfook2j7esad.onion, http://xqkz2rmrqkeqf6sjbrb47jfwnqxcd4o2zvaxxzrpbh2piknms37rw2ad.onion, http://gcbejm2rcjftouqbxuhimj5oroouqcuxb2my4raxqa7efkz5bd5464id.onion, http://griefcameifmv4hfr3auozmovz5yi6m3h3dwbuqw7baomfxoxz4qteid.onion, http://ws3dh6av66sjbxxkjpw5ao3wqzmtejnkzheswm4dz5rrwvular7xvkqd.onion/, http://ft4zr2jzlqoyob7yg4fcpwyt37hox3ajajqnfkdvbfrkjioyunmqnpad.onion, http://hiveleakdbtnp76ulyhi52eag6c6tyc3xw7ez7iqy6wc34gd2nekazyd.onion, http://matmq3z3hiovia3voe2tix2x54sghc3tszj74xgdy4tqtypoycszqzqd.onion, http://r6d636w47ncnaukrpvlhmtdbvbeltc6enfcuuow3jclpmyga7cz374qd.onion, http://kf6x3mjeqljqxjznaw65jixin7dpcunfxbbakwuitizytcpzn4iy5bad.onion, http://ncwkg6fbodo2dsuuxjqowuampdh6nukrha65fe7ghf3ywsiideplfkuad.onion/board/leak_list, http://spyarea23ttlty6qav3ecmbclpqym3p32lksanoypvrqm6j5onstsjad.onion, http://izis6oyht2suanp5fb5tsxqywwtww7ph5ho7vdjbtyzvs4hkidxgklid.onion, http://lhxxtrqraokn63f3nubhbjrzxkrgduq3qogp3yr424tkpvh3z7n4kcyd.onion, http://n3f7nxkjway3d223j27lyad7v5cgmyaifesycvmwq7i7cbs23lb6llryd.onion, http://3nvzqyo6l4wkrzumzu5aod7zbosq4ipgf7ifgj3hsvbcr5vcasordvqd.onion, http://leaktheanalyst.fireeye62c3da3fnosymmmcqcty7rl7cjucpbkzaz275a4qs5fgkzhad.onion, http://yeuajcizwytgmrntijhxphs6wn5txp2prs6rpndafbsapek3zd4ubcid.onion, http://lockbitapt6vx57t3eeqjofwgcglmutr3a35nygvokja5uuccip4ykyd.onion, http://nlockbitapt2yfbt7lchxejug47kmqvqqxvvjpqkmevv4l3azl3gy6pyd.onion, http://nlockbitapt5x4zkjbcqmz6frdhecqqgadevyiwqxukksspnlidyvd7qd.onion, http://nlockbitapt34kvrip6xojylohhxrwsvpzdffgs5z4pbbsywnzsbdguqd.onion, http://nlockbitaptc2iq4atewz2ise62q63wfktyrl4qtwuk5qax262kgtzjqd.onion, http://nlockbitaptjpikdqjynvgozhgc6bgetgucdk5xjacozeaawihmoio6yd.onion, http://nlockbitaptq7ephv2oigdncfhtwhpqgwmqojnxqdyhprxxfpcllqdxad.onion, http://nlockbitaptstzf3er2lz6ku3xuifafq2yh5lmiqj5ncur6rtlmkteiqd.onion, http://noyarbnujct53bizjguvolxou3rmuda2vr72osyexngbdkhqebwrzsnad.onion, http://lockbitapt2yfbt7lchxejug47kmqvqqxvvjpqkmevv4l3azl3gy6pyd.onion, http://nlockbitapt5x4zkjbcqmz6frdhecqqgadevyiwqxukksspnlidyvd7qd.onion, http://nlockbitapt6vx57t3eeqjofwgcglmutr3a35nygvokja5uuccip4ykyd.onion, http://nlockbitapt34kvrip6xojylohhxrwsvpzdffgs5z4pbbsywnzsbdguqd.onion, http://nlockbitaptc2iq4atewz2ise62q63wfktyrl4qtwuk5qax262kgtzjqd.onion, http://nlockbitaptjpikdqjynvgozhgc6bgetgucdk5xjacozeaawihmoio6yd.onion, http://nlockbitaptq7ephv2oigdncfhtwhpqgwmqojnxqdyhprxxfpcllqdxad.onion, http://nlockbitaptstzf3er2lz6ku3xuifafq2yh5lmiqj5ncur6rtlmkteiqd.onion, http://nlockbitaptoofrpignlz6dt2wqqc5z3a4evjevoa3eqdfcntxad5lmyd.onion, http://wm6mbuzipviusuc42kcggzkdpbhuv45sn7olyamy6mcqqked3waslbqd.onion, http://zqaflhty5hyziovsxgqvj2mrz5e5rs6oqxzb54zolccfnvtn5w2johad.onion, http://lorenzmlwpzgxq736jzseuterytjueszsvznuibanxomlpkyxk6ksoyd.onion, http://4qbxi3i2oqmyzxsjg4fwe4aly3xkped52gq5orp6efpkeskvchqe27id.onion, http://nrbvuetuneohce3ouxjlbxtimyyxokb4btncxjbo44fbgxqy7tskinwad.onion, http://wtyafjyhwqrgo4a45wdvvwhen3cx4euie73qvlhkhvlrexljoyuklaad.onion, http://jvdamsif53dqjycuozlaye2s47p7xij4x6hzwzwhzrqmv36gkyzohhqd.onion, http://nfvki3hj7uxuirxpeop6chgqoczanmebutznt2mkzy6waov6w456vjuid.onion, http://xembshruusobgbvxg4tcjs3jpdnks6xrr6nbokfxadcnlc53yxir22ad.onion, http://z6wkgghtoawog5noty5nxulmmt2zs7c3yvwr22v4czbffdoly2kl4uad.onion, http://midasbkic5eyfox4dhnijkzc7v7e4hpmsb2qgux7diqbpna4up4rtdad.onion/blog.php, http://nymnbqd5gmtxc2wepkesq2ktr5qf4uga6wwrsbtktq7n5uvhqmbyaq4qd.onion/blog.php, http://dfpc7yvle5kxmgg6sbcp5ytggy3oeob676bjgwcwhyr2pwcrmbvoilqd.onion, http://moishddxqnpdxpababec6exozpl2yr7idfhdldiz5525ao25bmasxhid.onion, http://mblogci3rudehaagbryjznltdp33ojwzkq6hn2pckvjq33rycmzczpid.onion, http://n, http://mosesstaffm7hptp.onion, http://n, http://mountnewsokhwilx.onion, http://n3twormruynhn3oetmxvasum2miix2jgg56xskdoyihra4wthvlgyeyd.onion, http://hxt254aygrsziejn.onion, http://gg5ryfgogainisskdvh4y373ap3b2mxafcibeh2lvq5x7fx76ygcosad.onion, http://lirncvjfmdhv6samxvvlohfqx7jklfxoxj7xn3fh7qeabs3taemdsdqd.onion, http://vfokxcdzjbpehgit223vzdzwte47l3zcqtafj34qrr26htjo4uf3obid.onion, http://n746pbrxl7acvrlhzshosye3b3udk4plurpxt2pp27pojfhkkaooqiiqd.onion, http://mrdxtxy6vqeqbmb4rvbvueh2kukb3e3mhu3wdothqn7242gztxyzycid.onion, http://hxxp://omegalock5zxwbhswbisc42o2q2i54vdulyvtqqbudqousisjgc7j7yd.onion/, http://n0mega.cc, http://vbfqeh5nugm6r2u2qvghsdxm3fotf5wbxb5ltv6vw77vus5frdpuaiid.onion, http://pay2key2zkg7arp3kv3cuugdaqwuesifnbofun4j6yjdw5ry7zw2asid.onion, http://vbmisqjshn4yblehk2vbnil53tlqklxsdaztgphcilto3vdj4geao5qd.onion, http://nwavbeudogz6byhnardd2lkp2jafims3j7tj6k6qnywchn2csngvtffqd.onion, http://mbrlkbtq5jonaqkurjwmxftytyn2ethqvbxfu4rgjbkkknndqwae6byd.onion/, http://promethw27cbrcot.onion/blog, http://pysa2bitc5ldeyfak4seeruqymqs4sj5wt5qkcq7aoyg4h2acqieywad.onion, http://kbsqoivihgdmwczmxkbovk7ss2dcynitwhhfu5yw725dboqo5kthfaad.onion, http://quantum445bh3gzuyilxdzs5xdepf3b7lkcupswvkryf3n7hgzpxebid.onion, http://p6o7m73ujalhgkiv.onion, http://nrgleak7op734elep.onion, http://nrgleaktxuey67yrgspmhvtnrqtgogur35lwdrup4d3igtbm3pupc4lyd.onion, http://wobpitin77vdsdiswr43duntv6eqw4rvphedutpaxycjdie6gg3binad.onion, http://sushlnty2j7qdzy64qnvyb6ajkwg7resd3p6agc2widnawodtcedgjid.onion, http://d57uremugxjrafyg.onion, http://rnsm777cdsjrsdlbs4v5qoeppu3px6sb2igmh53jzrx7ipcrbjz5b2ad.onion, http://xw7au5pnwtl6lozbsudkmyd32n6gnqdngitjdppybudan3x3pjgpmpid.onion, http://nt.me/ransom_house, http://blog2hkbm6gogpv2b3uytzi3bj5d5zmc4asbybumjkhuqhas355janyd.onion, http://relic5zqwemjnu4veilml6prgyedj6phs7de3udhicuq53z37klxm6qd.onion, http://blogxxu75w63ujqarv476otld7cyjkq4yoswzt4ijadkjwvg3vrvd5yd.onion, http://gamol6n6p2p4c3ad7gxmx3ur7wwdwlywebo2azv3vv5qlmjmole2zbyd.onion/, http://royal4ezp7xrbakkus3oofjw6gszrohpodmdnfbe5e4w3og5sm7vb3qd.onion, http://crptd5sv5bdz6hovrbkac6mnp3rt7zij62njsqwh5a6ldd3asxdd22qd.onion, http://hl66646wtlp2naoqnhattngigjp5palgqmbwixepcjyq5i534acgqyad.onion, http://nsnatch.vip, http://nsnatch.top, http://nsnatch.press, http://nsnatch.kim, http://zj2ex44e2b2xi43m2txk4uwi3l55aglsarre7repw7rkfwpj54j46iqd.onion, http://spookuhvfyxzph54ikjfwf2mwmxt572krpom7reyayrmxbkizbvkpaid.onion/blog/, http://nbzzb6sa6xuura2z.onion, http://nx2miyuiwpib2imjr5ykyjngdu7v6vprkkhjltrk4qafymtawey4qzwid.onion, http://4rbgxisigb4pxnloxzc265rmzaj7fslrhyouegtrph2a7xhh55r6xaid.onion, http://3udp4kspxiirvxop.onion, http://vsociethok6sbprvevl4dlwbqrzyhxcxaqpvcqt5belwvsuxaxsutyad., http://n4hzyuotli6maqa4u.onion, http://nalr2uqsave7y2r235am5jsfiklfjh5h4jc5nztu3rzvmhklwt5j6kid.onion, http://xingnewj6m4qytljhfwemngm7r7rogrindbq7wrfeepejgxc3bwci7qd.onion, http://jukswsxbh3jsxuddvidrjdvwuohtsy4kxg2axbppiyclomt2qciyfoad.onion"

# Split the input URLs into a list
url_list = input_urls.split(',')

# Create a list of dictionaries in the desired format
json_data = [{"group": url.strip()} for url in url_list]

# Write the JSON data to a file
with open('linkedin_urls.json', 'w') as json_file:
    json.dump(json_data, json_file, indent=4)

print("JSON data has been written to 'linkedin_urls.json'")
