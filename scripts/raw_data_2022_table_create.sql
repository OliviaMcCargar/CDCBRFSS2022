DROP TABLE IF EXISTS raw_data_2022;

CREATE TABLE raw_data_2022 (
     RESPONSE_ID SERIAL PRIMARY KEY,
     _STATE TEXT,
     FMONTH TEXT,
     IDATE TEXT,
     IMONTH TEXT,
     IDAY TEXT,
     IYEAR TEXT,
     DISPCODE TEXT,
     SEQNO TEXT,
     _PSU TEXT,
     CTELENM1 TEXT,
     PVTRESD1 TEXT,
     COLGHOUS TEXT,
     STATERE1 TEXT,
     CELPHON1 TEXT,
     LADULT1 TEXT,
     COLGSEX1 TEXT,
     NUMADULT TEXT,
     LANDSEX1 TEXT,
     NUMMEN TEXT,
     NUMWOMEN TEXT,
     RESPSLCT TEXT,
     SAFETIME TEXT,
     CTELNUM1 TEXT,
     CELLFON5 TEXT,
     CADULT1 TEXT,
     CELLSEX1 TEXT,
     PVTRESD3 TEXT,
     CCLGHOUS TEXT,
     CSTATE1 TEXT,
     LANDLINE TEXT,
     HHADULT TEXT,
     SEXVAR TEXT,
     GENHLTH TEXT,
     PHYSHLTH TEXT,
     MENTHLTH TEXT,
     POORHLTH TEXT,
     PRIMINSR TEXT,
     PERSDOC3 TEXT,
     MEDCOST1 TEXT,
     CHECKUP1 TEXT,
     EXERANY2 TEXT,
     SLEPTIM1 TEXT,
     LASTDEN4 TEXT,
     RMVTETH4 TEXT,
     CVDINFR4 TEXT,
     CVDCRHD4 TEXT,
     CVDSTRK3 TEXT,
     ASTHMA3 TEXT,
     ASTHNOW TEXT,
     CHCSCNC1 TEXT,
     CHCOCNC1 TEXT,
     CHCCOPD3 TEXT,
     ADDEPEV3 TEXT,
     CHCKDNY2 TEXT,
     HAVARTH4 TEXT,
     DIABETE4 TEXT,
     DIABAGE4 TEXT,
     MARITAL TEXT,
     EDUCA TEXT,
     RENTHOM1 TEXT,
     NUMHHOL4 TEXT,
     NUMPHON4 TEXT,
     CPDEMO1C TEXT,
     VETERAN3 TEXT,
     EMPLOY1 TEXT,
     CHILDREN TEXT,
     INCOME3 TEXT,
     PREGNANT TEXT,
     WEIGHT2 TEXT,
     HEIGHT3 TEXT,
     DEAF TEXT,
     BLIND TEXT,
     DECIDE TEXT,
     DIFFWALK TEXT,
     DIFFDRES TEXT,
     DIFFALON TEXT,
     HADMAM TEXT,
     HOWLONG TEXT,
     CERVSCRN TEXT,
     CRVCLCNC TEXT,
     CRVCLPAP TEXT,
     CRVCLHPV TEXT,
     HADHYST2 TEXT,
     HADSIGM4 TEXT,
     COLNSIGM TEXT,
     COLNTES1 TEXT,
     SIGMTES1 TEXT,
     LASTSIG4 TEXT,
     COLNCNCR TEXT,
     VIRCOLO1 TEXT,
     VCLNTES2 TEXT,
     SMALSTOL TEXT,
     STOLTEST TEXT,
     STOOLDN2 TEXT,
     BLDSTFIT TEXT,
     SDNATES1 TEXT,
     SMOKE100 TEXT,
     SMOKDAY2 TEXT,
     USENOW3 TEXT,
     ECIGNOW2 TEXT,
     LCSFIRST TEXT,
     LCSLAST TEXT,
     LCSNUMCG TEXT,
     LCSCTSC1 TEXT,
     LCSSCNCR TEXT,
     LCSCTWHN TEXT,
     ALCDAY4 TEXT,
     AVEDRNK3 TEXT,
     DRNK3GE5 TEXT,
     MAXDRNKS TEXT,
     FLUSHOT7 TEXT,
     FLSHTMY3 TEXT,
     PNEUVAC4 TEXT,
     TETANUS1 TEXT,
     HIVTST7 TEXT,
     HIVTSTD3 TEXT,
     HIVRISK5 TEXT,
     COVIDPOS TEXT,
     COVIDSMP TEXT,
     COVIDPRM TEXT,
     PDIABTS1 TEXT,
     PREDIAB2 TEXT,
     DIABTYPE TEXT,
     INSULIN1 TEXT,
     CHKHEMO3 TEXT,
     EYEEXAM1 TEXT,
     DIABEYE1 TEXT,
     DIABEDU1 TEXT,
     FEETSORE TEXT,
     TOLDCFS TEXT,
     HAVECFS TEXT,
     WORKCFS TEXT,
     IMFVPLA3 TEXT,
     HPVADVC4 TEXT,
     HPVADSHT TEXT,
     SHINGLE2 TEXT,
     COVIDVA1 TEXT,
     COVACGET TEXT,
     COVIDNU1 TEXT,
     COVIDINT TEXT,
     COVIDFS1 TEXT,
     COVIDSE1 TEXT,
     COPDCOGH TEXT,
     COPDFLEM TEXT,
     COPDBRTH TEXT,
     COPDBTST TEXT,
     COPDSMOK TEXT,
     CNCRDIFF TEXT,
     CNCRAGE TEXT,
     CNCRTYP2 TEXT,
     CSRVTRT3 TEXT,
     CSRVDOC1 TEXT,
     CSRVSUM TEXT,
     CSRVRTRN TEXT,
     CSRVINST TEXT,
     CSRVINSR TEXT,
     CSRVDEIN TEXT,
     CSRVCLIN TEXT,
     CSRVPAIN TEXT,
     CSRVCTL2 TEXT,
     PSATEST1 TEXT,
     PSATIME1 TEXT,
     PCPSARS2 TEXT,
     PSASUGST TEXT,
     PCSTALK1 TEXT,
     CIMEMLOS TEXT,
     CDHOUSE TEXT,
     CDASSIST TEXT,
     CDHELP TEXT,
     CDSOCIAL TEXT,
     CDDISCUS TEXT,
     CAREGIV1 TEXT,
     CRGVREL4 TEXT,
     CRGVLNG1 TEXT,
     CRGVHRS1 TEXT,
     CRGVPRB3 TEXT,
     CRGVALZD TEXT,
     CRGVPER1 TEXT,
     CRGVHOU1 TEXT,
     CRGVEXPT TEXT,
     ACEDEPRS TEXT,
     ACEDRINK TEXT,
     ACEDRUGS TEXT,
     ACEPRISN TEXT,
     ACEDIVRC TEXT,
     ACEPUNCH TEXT,
     ACEHURT1 TEXT,
     ACESWEAR TEXT,
     ACETOUCH TEXT,
     ACETTHEM TEXT,
     ACEHVSEX TEXT,
     ACEADSAF TEXT,
     ACEADNED TEXT,
     LSATISFY TEXT,
     EMTSUPRT TEXT,
     SDHISOLT TEXT,
     SDHEMPLY TEXT,
     FOODSTMP TEXT,
     SDHFOOD1 TEXT,
     SDHBILLS TEXT,
     SDHUTILS TEXT,
     SDHTRNSP TEXT,
     SDHSTRE1 TEXT,
     MARIJAN1 TEXT,
     MARJSMOK TEXT,
     MARJEAT TEXT,
     MARJVAPE TEXT,
     MARJDAB TEXT,
     MARJOTHR TEXT,
     USEMRJN4 TEXT,
     LASTSMK2 TEXT,
     STOPSMK2 TEXT,
     MENTCIGS TEXT,
     MENTECIG TEXT,
     HEATTBCO TEXT,
     ASBIALCH TEXT,
     ASBIDRNK TEXT,
     ASBIBING TEXT,
     ASBIADVC TEXT,
     ASBIRDUC TEXT,
     FIREARM5 TEXT,
     GUNLOAD TEXT,
     LOADULK2 TEXT,
     RCSGEND1 TEXT,
     RCSXBRTH TEXT,
     RCSRLTN2 TEXT,
     CASTHDX2 TEXT,
     CASTHNO2 TEXT,
     BIRTHSEX TEXT,
     SOMALE TEXT,
     SOFEMALE TEXT,
     TRNSGNDR TEXT,
     HADSEX TEXT,
     PFPPRVN4 TEXT,
     TYPCNTR9 TEXT,
     BRTHCNT4 TEXT,
     WHEREGET TEXT,
     NOBCUSE8 TEXT,
     BCPREFER TEXT,
     RRCLASS3 TEXT,
     RRCOGNT2 TEXT,
     RRTREAT TEXT,
     RRATWRK2 TEXT,
     RRHCARE4 TEXT,
     RRPHYSM2 TEXT,
     QSTVER TEXT,
     QSTLANG TEXT,
     _METSTAT TEXT,
     _URBSTAT TEXT,
     MSCODE TEXT,
     _STSTR TEXT,
     _STRWT TEXT,
     _RAWRAKE TEXT,
     _WT2RAKE TEXT,
     _IMPRACE TEXT,
     _CHISPNC TEXT,
     _CRACE2 TEXT,
     _CPRACE2 TEXT,
     CAGEG TEXT,
     _CLLCPWT TEXT,
     _DUALUSE TEXT,
     _DUALCOR TEXT,
     _LLCPWT2 TEXT,
     _LLCPWT TEXT,
     _RFHLTH TEXT,
     _PHYS14D TEXT,
     _MENT14D TEXT,
     _HLTHPLN TEXT,
     _HCVU652 TEXT,
     _TOTINDA TEXT,
     _EXTETH3 TEXT,
     _ALTETH3 TEXT,
     _DENVST3 TEXT,
     _MICHD TEXT,
     _LTASTH1 TEXT,
     _CASTHM1 TEXT,
     _ASTHMS1 TEXT,
     _DRDXAR2 TEXT,
     _PRACE2 TEXT,
     _MRACE2 TEXT,
     _HISPANC TEXT,
     _RACE1 TEXT,
     _RACEG22 TEXT,
     _RACEGR4 TEXT,
     _RACEPR1 TEXT,
     _SEX TEXT,
     _AGEG5YR TEXT,
     _AGE65YR TEXT,
     _AGE80 TEXT,
     _AGE_G TEXT,
     HTIN4 TEXT,
     HTM4 TEXT,
     WTKG3 TEXT,
     _BMI5 TEXT,
     _BMI5CAT TEXT,
     _RFBMI5 TEXT,
     _CHLDCNT TEXT,
     _EDUCAG TEXT,
     _INCOMG1 TEXT,
     _RFMAM22 TEXT,
     _MAM5023 TEXT,
     _HADCOLN TEXT,
     _CLNSCP1 TEXT,
     _HADSIGM TEXT,
     _SGMSCP1 TEXT,
     _SGMS101 TEXT,
     _RFBLDS5 TEXT,
     _STOLDN1 TEXT,
     _VIRCOL1 TEXT,
     _SBONTI1 TEXT,
     _CRCREC2 TEXT,
     _SMOKER3 TEXT,
     _RFSMOK3 TEXT,
     _CURECI2 TEXT,
     _YRSSMOK TEXT,
     _PACKDAY TEXT,
     _PACKYRS TEXT,
     _YRSQUIT TEXT,
     _SMOKGRP TEXT,
     _LCSREC TEXT,
     DRNKANY6 TEXT,
     DROCDY4_ TEXT,
     _RFBING6 TEXT,
     _DRNKWK2 TEXT,
     _RFDRHV8 TEXT,
     _FLSHOT7 TEXT,
     _PNEUMO3 TEXT,
     _AIDTST4 TEXT,
);