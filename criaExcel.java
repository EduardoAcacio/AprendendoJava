package com.cpqi.boletador;

import java.io.*;

import javax.swing.JOptionPane;

import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;

public class CriaMain {

	//public static void main(String[] args) throws IOException {
		//criando o arquivo
		FileOutputStream file = new FileOutputStream(new File("reg.xlsx"));
		
		//criando pasta de trabalho
		Workbook wb = new HSSFWorkbook();
		
		//criando a pasta
		Sheet planilha = wb.createSheet("Registros");
		
		//criando linha
		Row linha = planilha.createRow(0);
		
		//criando a celula
		Cell celula = linha.createCell(0);
		
		//preencher celula
		celula.setCellValue("Testando inserção");
		
		//escrever a stream no arquivo
		wb.write(file);
		
		//fechando arquivo
		file.close();
		
		JOptionPane.showMessageDialog(null, "Arquivo criado com sucesso.");
		
	}

}
