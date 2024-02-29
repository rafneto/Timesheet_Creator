import calendar
from fpdf import FPDF
from fpdf import FontFace
import pathlib
import argostranslate.package
import argostranslate.translate

DOC_HEADER_FONT_SIZE=16
DOC_HEADER_SIZE_ALT=8
DOC_FONT_SIZE=9
TABLE_HEADER_SIZE_ALT=6
from_code="en"
to_code="pt"

package_path=pathlib.Path(str(pathlib.Path.cwd())+"/translations/translate-en_pt-1_0.argosmodel")
argostranslate.package.install_from_path(package_path)

def translation(text):
    installed_languages=argostranslate.translate.get_installed_languages()
    from_lang=list(filter(
            lambda x:x.code==from_code,
            installed_languages))[0]
    to_lang=list(filter(
            lambda x:x.code==to_code,
            installed_languages))[0]
    translation=from_lang.get_translation(to_lang)
    translatedText=translation.translate(text)
    return translatedText

def get_list_of_days_weeks(month, year):
    weekdays_optimized=[]
    cal=calendar.Calendar(firstweekday=calendar.MONDAY)
    weekdays=cal.monthdays2calendar(year, month)
    for week in weekdays:
        for day in week:
            number,weekday=day
            if number > 0:
                weekdays_optimized.append((number, calendar.day_name[weekday]))
    return weekdays_optimized

def generate_pdf(list_items, headers):    
    
    translate_month=translation(headers.get("month"))
    pdf=FPDF(orientation="portrait", format="A4")
    pdf.set_font('helvetica', size=DOC_FONT_SIZE)    
    pdf.add_page()
    pdf.ln()
    pdf.ln()
    with pdf.table(text_align="CENTER", borders_layout="NONE") as table:
        row=table.row()
        row.cell(text="FOLHA DE REGISTO DE HORAS TRABALHADAS", style=FontFace(size_pt=DOC_HEADER_FONT_SIZE))
        
    pdf.ln()

    with pdf.table(text_align="LEFT", num_heading_rows=2, col_widths=(11,49,6,19,6,19)) as table:
        row=table.row()
        row.cell(text="Empregador", style=FontFace(size_pt=DOC_HEADER_SIZE_ALT))
        row.cell(headers.get("company"))
        row.cell(text="Sede", style=FontFace(size_pt=DOC_HEADER_SIZE_ALT))
        row.cell(headers.get("headoffice"))
        row.cell(text="Local", style=FontFace(size_pt=DOC_HEADER_SIZE_ALT))
        row.cell(headers.get("localoffice"))
        
        row=table.row()
        row.cell(text="Trabalhador", style=FontFace(size_pt=DOC_HEADER_SIZE_ALT))
        row.cell(headers.get("name"))
        row.cell(text="Mês", style=FontFace(size_pt=DOC_HEADER_SIZE_ALT))
        row.cell(translate_month)
        row.cell(text="Ano", style=FontFace(size_pt=DOC_HEADER_SIZE_ALT))
        row.cell(headers.get("year"))
    
    pdf.ln()
        
    with pdf.table(text_align="CENTER", num_heading_rows=2, col_widths=(10, 10, 10, 10, 10, 25, 25)) as table:
        heading=table.row()
        heading.cell("DIAS", rowspan=2)
        heading.cell("1º Período", colspan=2)
        heading.cell("2º Período", colspan=2)
        heading.cell("Observações", rowspan=2)
        heading.cell("Assinatura", rowspan=2)
        
        heading=table.row()
        heading.cell(text="ENTRADA\n(HORA)", style=FontFace(size_pt=TABLE_HEADER_SIZE_ALT))
        heading.cell(text="SAÍDA\n(HORA)", style=FontFace(size_pt=TABLE_HEADER_SIZE_ALT))
        heading.cell(text="ENTRADA\n(HORA)", style=FontFace(size_pt=TABLE_HEADER_SIZE_ALT))
        heading.cell(text="SAÍDA\n(HORA)", style=FontFace(size_pt=TABLE_HEADER_SIZE_ALT))
                
        for item in list_items:
            print(item)
            if item.get("obs") != '---':
                translate_obs=translation(item.get("obs"))
            else:
                translate_obs="---"
            row = table.row()
            style = FontFace(fill_color=255)
            if item.get("isWeekend"):
                style = FontFace(fill_color=200)
                            
            row.cell(text=item.get("day"), style=style)
            if item.get("checkbox") == 0:
                row.cell(text="---", style=style)
                row.cell(text="---", style=style)
            else:
                row.cell(text="09:00")
                row.cell(text="13:00")
                
            if item.get("checkbox2") == 0:
                row.cell(text="---", style=style)
                row.cell(text="---", style=style)
            else:
                row.cell(text="14:00")
                row.cell(text="18:00")
            row.cell(text=translate_obs, style=style)
            row.cell(text="", style=style)
    file_name = translate_month+"-"+headers.get("year")+".pdf"
    pdf.output(file_name)
    return file_name
