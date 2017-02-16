package com.cpqi.formata;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.Iterator;
import javax.swing.JOptionPane;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

public class FormatadorMain {

	public static void main(String[] args) throws IOException {
		//criando o arquivo
		FileInputStream file = new FileInputStream(new File("manip.xlsx"));

		//criando pasta de trabalho
		XSSFWorkbook wb = new XSSFWorkbook(file);

		//criando planilha
		XSSFSheet planilha = wb.getSheetAt(0);

		//lendo as linhas
		Iterator<Row> linhas = planilha.iterator();

		//laço
		while(linhas.hasNext()){

			String ln = "";
			//criar linha
			Row linha = linhas.next();

			//iterador varendo as celulas
			Iterator<Cell> celulas = linha.iterator();

			//laço para iterar celuals
			while(celulas.hasNext()){

				//criando celula
				Cell celula = celulas.next();

				switch (celula.getCellType()) {
				
				case Cell.CELL_TYPE_STRING:
					ln += celula.getStringCellValue();
					break;

				case Cell.CELL_TYPE_NUMERIC:
					ln += celula.getNumericCellValue();
					break;

				default:
					break;
				}	
			}
			System.out.println(ln);
		}
		file.close();
		JOptionPane.showMessageDialog(null, "Foi!");
	}

}
